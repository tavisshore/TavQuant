# Generated by Django 4.2.5 on 2023-09-30 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0007_rename_accumulated_depreciation_amortization_ppe_balance_accumulateddepreciationamortizationppe_and_'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balance',
            old_name='accumulatedDepreciationAmortizationPpe',
            new_name='accumulatedDepreciationAmortizationPPE',
        ),
        migrations.RenameField(
            model_name='balance',
            old_name='date',
            new_name='fiscalDateEnding',
        ),
        migrations.RenameField(
            model_name='balance',
            old_name='currency',
            new_name='reportedCurrency',
        ),
        migrations.RenameField(
            model_name='balance',
            old_name='totalNonCurrent_liabilities',
            new_name='totalNonCurrentLiabilities',
        ),
        migrations.RenameField(
            model_name='cash',
            old_name='date',
            new_name='fiscalDateEnding',
        ),
    ]