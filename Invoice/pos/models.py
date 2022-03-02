from django.db import models


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
    other_buyer_id = models.CharField(max_length=150, null=True, blank=True)


class Buyer(models.Model):
    organization_name = models.CharField(max_length=300, null=True, blank=True)
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
    date_of_supply = models.DateField(null=True, blank=True)
    reference_number = models.CharField(max_length=150, null=True, blank=True)
    branch = models.CharField(max_length=300, null=True, blank=True)
    salesman_name = models.CharField(max_length=300, null=True, blank=True)
    invoice_number = models.CharField(max_length=150, null=True, blank=True)
    invoice_issue_date = models.DateTimeField(auto_now=False)
    page_number = models.IntegerField(null=True, blank=True)


class Product(models.Model):
    item_code = models.CharField(max_length=100, null=True, blank=True)
    item_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)


class Pos(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE, null=True, blank=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    item_code = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    vat_percent = models.FloatField(null=True, blank=True)
    vat = models.FloatField(null=True, blank=True)
    value = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total = self.quantity * self.price
        self.vat = self.total * self.vat_percent / 100
        self.value = self.total + self.vat

        super(Pos, self).save(*args, **kwargs)
