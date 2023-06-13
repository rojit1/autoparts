# Generated by Django 4.0.6 on 2023-06-13 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_bill_generated'),
        ('bill', '0005_alter_bill_fiscal_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order'),
        ),
    ]
