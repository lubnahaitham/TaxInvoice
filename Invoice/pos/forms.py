from django import forms
from .models import Setting, Buyer, Invoice, Product, Pos


class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = ['organization_name', 'building_number', 'street_name', 'district', 'city', 'country',
                  'postal_code', 'additional_number', 'vat_number', 'other_buyer_id']

    labels = {
        'organization_name': 'Organization Name',
        'building_number': 'Building Number',
        'street_name': 'Street Name',
        'district': 'District',
        'city': 'City',
        'country': 'Country',
        'postal_code': 'Postal Code',
        'additional_number': 'Additional Number',
        'vat_number': 'Vat Number',
        'other_buyer_id': 'Other Buyer Id'
    }


class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['organization_name', 'building_number', 'street_name', 'district', 'city', 'country',
                  'postal_code', 'additional_number', 'vat_number', 'other_buyer_id']

    labels = {
        'organization_name': 'Organization Name',
        'building_number': 'Building Number',
        'street_name': 'Street Name',
        'district': 'District',
        'city': 'City',
        'country': 'Country',
        'postal_code': 'Postal Code',
        'additional_number': 'Additional Number',
        'vat_number': 'Vat Number',
        'other_buyer_id': 'Other Buyer Id'
    }


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['date_of_supply', 'reference_number', 'branch', 'salesman_name', 'invoice_number',
                  'invoice_issue_date', 'page_number']
        widgets = {
            'date_of_supply': forms.SelectDateWidget()
        }

    labels = {
        'date_of_supply': 'Date Of Supply',
        'reference_number': 'Reference Number',
        'branch': 'Branch',
        'salesman_name': 'Sales Man Name',
        'invoice_number': 'Invoice Number',
        'invoice_issue_date': 'Invoice Issue Date',
        'page_number': 'Page Number'
    }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['item_code', 'item_name', 'description', 'price']

    labels = {
        'item_code': 'Item Code',
        'item_name': 'Item Name',
        'description': 'Description',
        'price': 'Price'
    }


class PosForm(forms.ModelForm):
    class Meta:
        model = Pos
        fields = ['item_code', 'description', 'price', 'quantity', 'discount', 'total',
                  'vat_percent', 'vat']

    labels = {
        'item_code': 'Item Code',
        'description': 'Description',
        'price': 'Price',
        'quantity': 'Quantity',
        'discount': 'Discount',
        'total': 'Total',
        'vat_percent': 'Vat %',
        'vat': 'VAT',

    }
