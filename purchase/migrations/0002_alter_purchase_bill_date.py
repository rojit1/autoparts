# Generated by Django 4.0.6 on 2023-06-05 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='bill_date',
            field=models.DateField(default='2023-06-05', max_length=50),
            preserve_default=False,
        ),
    ]
