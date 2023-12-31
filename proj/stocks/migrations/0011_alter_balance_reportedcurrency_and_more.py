# Generated by Django 4.2.5 on 2023-09-30 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0010_overview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='reportedCurrency',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='cash',
            name='reportedCurrency',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='income',
            name='reportedCurrency',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='overview',
            name='Address',
            field=models.CharField(max_length=320),
        ),
        migrations.AlterField(
            model_name='overview',
            name='AssetType',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='overview',
            name='CIK',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='overview',
            name='Country',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='overview',
            name='Currency',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='overview',
            name='Exchange',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='overview',
            name='FiscalYearEnd',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='overview',
            name='Industry',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='overview',
            name='LatestQuarter',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='overview',
            name='Name',
            field=models.CharField(max_length=320),
        ),
        migrations.AlterField(
            model_name='overview',
            name='Sector',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='overview',
            name='Symbol',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock',
            field=models.CharField(max_length=32),
        ),
    ]
