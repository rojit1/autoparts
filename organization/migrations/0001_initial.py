# Generated by Django 4.0.6 on 2023-05-30 03:56

from django.db import migrations, models
import django.db.models.deletion
import organization.models
import root.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('sorting_order', models.IntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('org_name', models.CharField(max_length=255)),
                ('org_logo', models.ImageField(blank=True, null=True, upload_to='organization/images/')),
                ('tax_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='PAN/VAT Number')),
                ('website', models.URLField(blank=True, null=True)),
                ('current_fiscal_year', models.CharField(max_length=20, null=True)),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('company_contact_number', models.CharField(blank=True, max_length=255, null=True)),
                ('company_contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_person_name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_person_number', models.CharField(blank=True, max_length=255, null=True)),
                ('company_address', models.CharField(blank=True, max_length=255, null=True)),
                ('company_bank_qr', models.ImageField(blank=True, null=True, upload_to='organization/images/')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
            bases=(root.utils.SingletonModel, models.Model),
        ),
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('sorting_order', models.IntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('sorting_order', models.IntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=50, null=True)),
                ('branch_manager', models.CharField(blank=True, max_length=255, null=True)),
                ('branch_code', models.CharField(default=organization.models.get_default_uuid, max_length=255, unique=True)),
                ('is_central_billing', models.BooleanField(default=False, verbose_name='For Central Billing (Web)')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
