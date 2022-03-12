import segno
from django.db import models

from django.utils.timezone import now
from io import BytesIO
import base64
from datetime import datetime
from django.core.files.base import ContentFile


# Create your models here.

class Setting(models.Model):
    organization_name = models.CharField(max_length=300, null=True, blank=True)
    building_number = models.IntegerField(null=True, blank=True)
    street_name = models.CharField(max_length=150, null=True, blank=True)
    district = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=300, null=True, blank=True)
    country = models.CharField(max_length=300, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    additional_number = models.CharField(max_length=150, null=True, blank=True)
    vat_number = models.IntegerField(null=True, blank=True)
    other_seller_id = models.CharField(max_length=150, null=True, blank=True)


class Buyer(models.Model):
    buyer_organization_name = models.CharField(max_length=200, null=True, blank=True)
    building_number = models.IntegerField(null=True, blank=True)
    street_name = models.CharField(max_length=150, null=True, blank=True)
    district = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=300, null=True, blank=True)
    country = models.CharField(max_length=300, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    additional_number = models.CharField(max_length=150, null=True, blank=True)
    vat_number = models.IntegerField(null=True, blank=True)
    other_buyer_id = models.CharField(max_length=150, null=True, blank=True)


class Invoice(models.Model):
    """This is the client data model, it holds all client information. This
           docstring has to be improved."""

    def number():
        no = Invoice.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    date_of_supply = models.DateField(null=True, blank=True)
    branch = models.CharField(max_length=300, null=True, blank=True)
    salesman_name = models.CharField(max_length=300, null=True, blank=True)
    invoice_number = models.IntegerField(null=True, blank=True, unique=True, default=number)
    invoice_issue_date = models.DateTimeField(default=now, null=True, blank=True)
    page_number = models.IntegerField(null=True, blank=True)


class Product(models.Model):
    item_code = models.CharField(max_length=100, null=True, blank=True)
    item_name_in_arabic = models.CharField(max_length=200, null=True, blank=True)
    item_name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)


class Pos(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE, null=True, blank=True)
    item_code = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    unit_price = models.FloatField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    taxable_amount = models.FloatField(null=True, blank=True)
    tax_amount = models.FloatField(null=True, blank=True)
    tax_rate = models.FloatField(null=True, blank=True)
    total_vat = models.FloatField(null=True, blank=True)
    total_taxable_amount_exclude_vat = models.FloatField(null=True, blank=True)
    total_exclude_vat = models.FloatField(null=True, blank=True)
    total_amount_due = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    sub_total = models.FloatField(null=True, blank=True)
    # qr = models.ImageField(upload_to='', blank=True)

    def save(self, *args, **kwargs):
        self.taxable_amount = self.unit_price * self.quantity
        self.tax_amount = self.taxable_amount * self.tax_rate / 100
        self.sub_total = self.taxable_amount + self.tax_amount

        self.total_exclude_vat = self.taxable_amount
        self.total_taxable_amount_exclude_vat = self.taxable_amount
        self.total_vat = self.tax_amount
        self.total_amount_due = self.total_vat + self.total_exclude_vat

        super(Pos, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     now = datetime.now()
    #     year = now.strftime("%Y")
    #     month = now.strftime("%m")
    #     day = now.strftime("%d")
    #     date = str(day) + "-" + str(month) + "-" + str(year)
    #     # date = str(datetime.now().today())
    #     time = now.strftime("%H-%M")
    #     # time = str(datetime.now().strftime("%HH:"))
    #     data = str(self.setting.organization_name) + " " + str(self.setting.vat_number) + " " + str(self.total_amount_due) + " " + str(
    #         self.total_vat) + " " + str(date) + " " + str(time)
    #     print(data)
    #     data = data.encode("utf-8")
    #     data = base64.b64encode(data)
    #     # url = qrcode.make(data)
    #     print(data)
    #     out = BytesIO()
    #     qr = segno.make(data)
    #     qr.save(out, kind='png', dark='#000000', light=None, scale=6)
    #
    #     filename = 'qr-' + self.setting.organization_name + '.png'
    #     self.qr.save(filename, ContentFile(out.getvalue()), save=False)
    #
    #     super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     self.total = self.quantity * self.price
    #     self.vat = self.total * self.vat_percent / 100
    #     self.value = self.total + self.vat
    #
    #     super(Pos, self).save(*args, **kwargs)


class CloseInvoice(models.Model):
    organization_name = models.CharField(max_length=300, null=True, blank=True, verbose_name='organization_name')
    building_number = models.IntegerField(null=True, blank=True)
    street_name = models.CharField(max_length=150, null=True, blank=True)
    district = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=300, null=True, blank=True)
    country = models.CharField(max_length=300, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    additional_number = models.CharField(max_length=150, null=True, blank=True)
    vat_number = models.IntegerField(null=True, blank=True)
    other_seller_id = models.CharField(max_length=150, null=True, blank=True)
    organization_name_buyer = models.CharField(max_length=300, null=True, blank=True)
    building_number_buyer = models.IntegerField(null=True, blank=True)
    street_name_buyer = models.CharField(max_length=150, null=True, blank=True)
    district_buyer = models.CharField(max_length=150, null=True, blank=True)
    city_buyer = models.CharField(max_length=300, null=True, blank=True)
    country_buyer = models.CharField(max_length=300, null=True, blank=True)
    postal_code_buyer = models.IntegerField(null=True, blank=True)
    additional_number_buyer = models.CharField(max_length=150, null=True, blank=True)
    vat_number_buyer = models.IntegerField(null=True, blank=True)
    other_buyer_id = models.CharField(max_length=150, null=True, blank=True)
    date_of_supply = models.DateField(null=True, blank=True)
    reference_number = models.CharField(max_length=150, null=True, blank=True)
    branch = models.CharField(max_length=300, null=True, blank=True)
    salesman_name = models.CharField(max_length=300, null=True, blank=True)
    invoice_number = models.CharField(max_length=150, null=True, blank=True)
    invoice_issue_date = models.DateTimeField(auto_now=False)
    page_number = models.IntegerField(null=True, blank=True)
    item_code = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    vat_percent = models.FloatField(null=True, blank=True)
    vat = models.FloatField(null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
