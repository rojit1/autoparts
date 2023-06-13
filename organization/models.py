from django.db import models
from root.utils import BaseModel, SingletonModel
from django.db.models.signals import post_save
from django.dispatch import receiver
import environ
env = environ.Env(DEBUG=(bool, False))

class StaticPage(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    published_date = models.DateField(null=True, blank=True)
    keywords = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Organization(SingletonModel, BaseModel):
    # basic company details
    org_name = models.CharField(max_length=255)
    org_logo = models.ImageField(
        upload_to="organization/images/", null=True, blank=True
    )
    tax_number = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="PAN/VAT Number"
    )
    website = models.URLField(null=True, blank=True)
    current_fiscal_year = models.CharField(null=True, max_length=20)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    # contact details
    company_contact_number = models.CharField(max_length=255, null=True, blank=True)
    company_contact_email = models.EmailField(null=True, blank=True)
    contact_person_name = models.CharField(max_length=255, null=True, blank=True)
    contact_person_number = models.CharField(max_length=255, null=True, blank=True)
    company_address = models.CharField(max_length=255, null=True, blank=True)
    company_bank_qr = models.ImageField(
        upload_to="organization/images/", null=True, blank=True
    )

    def __str__(self):
        return self.org_name
    
    def get_fiscal_year(self):
        return f'{self.start_year}-{self.end_year}'



from uuid import uuid4


def get_default_uuid():
    return uuid4().hex


class Branch(BaseModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    contact_number = models.CharField(max_length=50, null=True, blank=True)
    branch_manager = models.CharField(max_length=255, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    branch_code = models.CharField(
        max_length=255, null=False, blank=False, unique=True, default=get_default_uuid
    )
    is_central_billing = models.BooleanField(default=False, verbose_name='For Central Billing (Web)')

    def __str__(self):
        return f"{self.organization.org_name} - {self.name} Branch"


class EndDayRecord(BaseModel):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    terminal = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.branch.name
    

class MailRecipient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MailSendRecord(models.Model):
    mail_recipient = models.ForeignKey(MailRecipient, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mail_recipient.name


class EndDayDailyReport(BaseModel):
    employee_name = models.CharField(max_length=50)
    net_amount = models.FloatField()
    total_amount = models.FloatField()
    vat = models.FloatField()
    total_discounts = models.FloatField()
    date_time = models.CharField(max_length=100, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    total_orders = models.IntegerField(default=0)

    def __str__(self):
        return 'Report'
    

from .utils import send_mail_to_receipients
from threading import Thread
from datetime import datetime

@receiver(post_save, sender=EndDayDailyReport)
def create_profile(sender, instance, created, **kwargs):
    if created:
        sender = env('EMAIL_HOST_USER')
        mail_list = []
        recipients = MailRecipient.objects.filter(status=True)
        for r in recipients:
            mail_list.append(r.email)
            MailSendRecord.objects.create(mail_recipient=r)
        if mail_list:
            dt_now = datetime.now()
            date_now = dt_now.date()
            time_now = dt_now.time().strftime('%I:%M %p')
            org = Organization.objects.first().org_name
            report_data = {
                'org_name':org,
                'date_now': date_now,
                'time_now': time_now,
                'total_amount': instance.total_amount,
                'date_time':instance.date_time,
                'employee_name': instance.employee_name,
                'net_amount': instance.net_amount,
                'vat': instance.vat,  
                'total_discounts': instance.total_discounts,
                'total_orders': instance.total_orders,
                'branch': instance.branch.name,
            }
            Thread(target=send_mail_to_receipients, args=(report_data, mail_list, sender)).start()