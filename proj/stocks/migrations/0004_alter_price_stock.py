# Generated by Django 4.2.5 on 2023-09-29 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_price_volume_alter_price_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.stock'),
        ),
    ]