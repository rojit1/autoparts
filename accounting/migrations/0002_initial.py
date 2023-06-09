# Generated by Django 4.0.6 on 2023-05-30 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('purchase', '0001_initial'),
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='depreciation',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.assetpurchaseitem'),
        ),
        migrations.AddField(
            model_name='depreciation',
            name='ledger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.accountledger'),
        ),
        migrations.AddField(
            model_name='cumulativeledger',
            name='account_chart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.accountchart'),
        ),
        migrations.AddField(
            model_name='accountsubledger',
            name='ledger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.accountledger'),
        ),
        migrations.AddField(
            model_name='accountledger',
            name='account_chart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.accountchart'),
        ),
        migrations.AlterUniqueTogether(
            name='fiscalyearsubledger',
            unique_together={('sub_ledger_name', 'fiscal_year')},
        ),
        migrations.AlterUniqueTogether(
            name='fiscalyearledger',
            unique_together={('ledger_name', 'fiscal_year')},
        ),
    ]
