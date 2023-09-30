from django.db import models

class Stock(models.Model):
    stock = models.CharField(max_length=32)
    interval = models.CharField(max_length=8)
    last_updated = models.DateTimeField("last updated")

    # Optional Derived Attributes
    #  = models.FloatField(blank=True, default='')

    def __str__(self):
        return str(self.stock)

class Overview(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    Symbol = models.CharField(max_length=32)
    AssetType = models.CharField(max_length=32)
    Name = models.CharField(max_length=320)
    Description = models.TextField()
    CIK = models.CharField(max_length=32)
    Exchange = models.CharField(max_length=32)
    Currency = models.CharField(max_length=32)
    Country = models.CharField(max_length=32)
    Sector = models.CharField(max_length=32)
    Industry = models.CharField(max_length=32)
    Address = models.CharField(max_length=320)
    FiscalYearEnd = models.CharField(max_length=32)
    LatestQuarter = models.CharField(max_length=32)
    MarketCapitalization = models.FloatField()
    EBITDA = models.FloatField()
    PERatio = models.FloatField()
    PEGRatio = models.FloatField()
    BookValue = models.FloatField()
    DividendPerShare = models.FloatField()
    DividendYield = models.FloatField()
    EPS = models.FloatField()
    RevenuePerShareTTM = models.FloatField()
    ProfitMargin = models.FloatField()
    OperatingMarginTTM = models.FloatField()
    ReturnOnAssetsTTM = models.FloatField()
    ReturnOnEquityTTM = models.FloatField()
    RevenueTTM = models.FloatField()
    GrossProfitTTM = models.FloatField()
    DilutedEPSTTM = models.FloatField()
    QuarterlyEarningsGrowthYOY = models.FloatField()
    QuarterlyRevenueGrowthYOY = models.FloatField()
    AnalystTargetPrice = models.FloatField()
    TrailingPE = models.FloatField()
    ForwardPE = models.FloatField()
    PriceToSalesRatioTTM = models.FloatField()
    PriceToBookRatio = models.FloatField()
    EVToRevenue = models.FloatField()
    EVToEBITDA = models.FloatField()
    Beta = models.FloatField()

    FiftyTwoWeekHigh = models.FloatField()
    FiftyTwoWeekLow = models.FloatField()
    FiftyDayMovingAverage = models.FloatField()
    TwoHundredDayMovingAverage = models.FloatField()
    SharesOutstanding = models.FloatField()

    DividendDate = models.DateTimeField("date")
    ExDividendDate = models.DateTimeField("date")
    def __str__(self):
        return self.stock.stock
    
class Price(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    interval = models.CharField(max_length=8)
    date = models.DateTimeField("date")
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()
    def __str__(self):
        return self.stock.stock

class Balance(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    fiscalDateEnding = models.DateTimeField("date")
    reportedCurrency = models.CharField(max_length=32)
    totalAssets = models.FloatField()
    totalCurrentAssets = models.FloatField()
    cashAndCashEquivalentsAtCarryingValue = models.FloatField()
    cashAndShortTermInvestments = models.FloatField()
    inventory = models.FloatField()
    currentNetReceivables = models.FloatField()
    totalNonCurrentAssets = models.FloatField()
    propertyPlantEquipment = models.FloatField()
    accumulatedDepreciationAmortizationPPE = models.FloatField()
    intangibleAssets = models.FloatField()
    intangibleAssetsExcludingGoodwill = models.FloatField()
    goodwill = models.FloatField()
    investments = models.FloatField()
    longTermInvestments = models.FloatField()
    shortTermInvestments = models.FloatField()
    otherCurrentAssets = models.FloatField()
    otherNonCurrentAssets = models.FloatField()
    totalLiabilities = models.FloatField()
    totalCurrentLiabilities = models.FloatField()
    currentAccountsPayable = models.FloatField()
    deferredRevenue = models.FloatField()
    currentDebt = models.FloatField()
    shortTermDebt = models.FloatField()
    totalNonCurrentLiabilities = models.FloatField()
    capitalLeaseObligations = models.FloatField()
    longTermDebt = models.FloatField()
    currentLongTermDebt = models.FloatField()
    longTermDebtNoncurrent = models.FloatField()
    shortLongTermDebtTotal = models.FloatField()
    otherCurrentLiabilities = models.FloatField()
    otherNonCurrentLiabilities = models.FloatField()
    totalShareholderEquity = models.FloatField()
    treasuryStock = models.FloatField()
    retainedEarnings = models.FloatField()
    commonStock = models.FloatField()
    commonStockSharesOutstanding = models.FloatField()
    def __str__(self):
        return self.stock.stock

class Cash(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    fiscalDateEnding = models.DateTimeField("date")
    reportedCurrency = models.CharField(max_length=32)
    operatingCashflow = models.FloatField()
    paymentsForOperatingActivities = models.FloatField()
    proceedsFromOperatingActivities = models.FloatField()
    changeInOperatingLiabilities = models.FloatField()
    changeInOperatingAssets = models.FloatField()
    depreciationDepletionAndAmortization = models.FloatField()
    capitalExpenditures = models.FloatField()
    changeInReceivables = models.FloatField()
    changeInInventory = models.FloatField()
    profitLoss = models.FloatField()
    cashflowFromInvestment = models.FloatField()
    cashflowFromFinancing = models.FloatField()
    proceedsFromRepaymentsOfShortTermDebt = models.FloatField()
    paymentsForRepurchaseOfCommonStock = models.FloatField()
    paymentsForRepurchaseOfEquity = models.FloatField()
    paymentsForRepurchaseOfPreferredStock = models.FloatField()
    dividendPayout = models.FloatField()
    dividendPayoutCommonStock = models.FloatField()
    dividendPayoutPreferredStock = models.FloatField()
    proceedsFromIssuanceOfCommonStock = models.FloatField()
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet = models.FloatField()
    proceedsFromIssuanceOfPreferredStock = models.FloatField()
    proceedsFromRepurchaseOfEquity = models.FloatField()
    proceedsFromSaleOfTreasuryStock = models.FloatField()
    changeInCashAndCashEquivalents = models.FloatField()
    changeInExchangeRate = models.FloatField()
    netIncome = models.FloatField()
    def __str__(self):
        return self.stock.stock

class Income(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    fiscalDateEnding = models.DateTimeField("date")
    reportedCurrency = models.CharField(max_length=32)
    grossProfit = models.FloatField()
    totalRevenue = models.FloatField()
    costOfRevenue = models.FloatField()
    costofGoodsAndServicesSold = models.FloatField()
    operatingIncome = models.FloatField()
    sellingGeneralAndAdministrative = models.FloatField()
    researchAndDevelopment = models.FloatField()
    operatingExpenses = models.FloatField()
    investmentIncomeNet = models.FloatField()
    netInterestIncome = models.FloatField()
    interestIncome = models.FloatField()
    interestExpense = models.FloatField()
    nonInterestIncome = models.FloatField()
    otherNonOperatingIncome = models.FloatField()
    depreciation = models.FloatField()
    depreciationAndAmortization = models.FloatField()
    incomeBeforeTax = models.FloatField()
    incomeTaxExpense = models.FloatField()
    interestAndDebtExpense = models.FloatField()
    netIncomeFromContinuingOperations = models.FloatField()
    comprehensiveIncomeNetOfTax = models.FloatField()
    ebit = models.FloatField()
    ebitda = models.FloatField()
    netIncome = models.FloatField()
    def __str__(self):
        return self.stock.stock


