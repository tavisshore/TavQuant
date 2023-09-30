# Create your tasks here
import os
from stocks.models import Stock, Price, Balance, Income, Cash, Overview
from celery import shared_task
import celery
from celery import app
from django_pandas.io import read_frame
import pandas as pd
import datetime

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.fundamentaldata import FundamentalData


# Keep this in a better location
ALPHA_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

def replace_none(test_dict):
    for key in test_dict:
        if test_dict[key] is None or test_dict[key] == 'None':
            test_dict[key] = 0
    return test_dict

def update_info_db(stock_object, ticker, fs, DB_object):
    exists = DB_object.objects.filter(stock=stock_object).exists()
    if exists: obj = DB_object.objects.filter(stock=stock_object).latest('fiscalDateEnding')
    if DB_object == Income: df = pd.DataFrame.from_dict(fs.get_income_statement_quarterly(ticker)[0])
    elif DB_object == Balance: df = pd.DataFrame.from_dict(fs.get_balance_sheet_quarterly(ticker)[0])
    elif DB_object == Cash: df = pd.DataFrame.from_dict(fs.get_cash_flow_quarterly(ticker)[0])
    elif DB_object == Overview: df = pd.DataFrame.from_dict(fs.get_company_overview(ticker)[0])
        
    df['fiscalDateEnding'] = pd.to_datetime(df['fiscalDateEnding'])
    if DB_object.objects.filter(stock=stock_object).exists(): df = df[df['fiscalDateEnding'] > obj.fiscalDateEnding]
    for row in df.iterrows():
        info_dict = row[1].to_dict()
        info_dict['stock'] = stock_object
        if DB_object == Overview:
            info_dict['FiftyTwoWeekHigh'] = info_dict.pop('52WeekHigh')
            info_dict['FiftyTwoWeekLow'] = info_dict.pop('52WeekLow')
            info_dict['FiftyDayMovingAverage'] = info_dict.pop('50DayMovingAverage')
            info_dict['TwoHundredDayMovingAverage'] = info_dict.pop('200DayMovingAverage')
        info_dict = replace_none(info_dict)
        info = DB_object(**info_dict)
        info.save()


@shared_task
def update_stock_data():
    today = datetime.date.today()
    stocks = Stock.objects.all()
    stocks = read_frame(stocks, column_names=['id', 'stock', 'interval', 'last_updated'])
    intervals = stocks['interval'].unique()
    list_to_update = []
    for j in intervals: 
        for i in stocks.iterrows():
            date = pd.to_datetime(i[1]['last_updated']).date()
            if date != today:
                list_to_update.append({'stock': i[1]['stock'], 'interval': j, 'last_updated': date})

    if list_to_update:
        ts = TimeSeries(ALPHA_KEY)
        fs = FundamentalData(ALPHA_KEY)
        today = pd.to_datetime(today)
        for stock in list_to_update: 
            ticker = stock['stock']
            interval = stock['interval']
            last_updated = stock['last_updated']
            # download_stock(ticker, interval)
            stock_object = Stock.objects.get(stock=ticker, interval=interval)
            if interval == 'daily': 
                stk, meta = ts.get_daily(symbol=ticker, outputsize='compact')
                stk = pd.DataFrame.from_dict(stk).T
            else: 
                stk, meta = ts.get_intraday(symbol=ticker, interval=interval, outputsize='compact')
                stk = pd.DataFrame.from_dict(stk).T
            stk.columns = ['open', 'high', 'low', 'close', 'volume']
            stk.index.name = 'date'
            # reduce to rows that are later than the today variable
            dates = pd.DataFrame([pd.to_datetime(i, format='%Y-%m-%d').date() for i in stk.index])[0]
            stk.index = dates
            stk = stk[stk.index > last_updated]

            for day in stk.iterrows():
                # Append Price values
                price = Price(stock=stock_object,
                            interval=interval,
                            date=day[0],
                            open=day[1]['open'],
                            high=day[1]['high'],
                            low=day[1]['low'],
                            close=day[1]['close'],
                            volume=day[1]['volume'])
                price.save()

            # check overview latest record date
            update_info_db(stock_object, ticker, fs, Overview)
            update_info_db(stock_object, ticker, fs, Income)
            update_info_db(stock_object, ticker, fs, Balance)
            update_info_db(stock_object, ticker, fs, Cash)

            Stock.objects.filter(stock=ticker).update(last_updated=today)











