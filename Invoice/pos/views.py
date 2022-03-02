from django.shortcuts import render, get_object_or_404, redirect

from .forms import SettingForm, BuyerForm, InvoiceForm, ProductForm, PosForm
from .models import Setting, Buyer, Invoice, Product, Pos


# Create your views here.
#
# def setting_list(request):
#     context = {'setting_list': Setting.objects.all()}
#     return render(request, "setting/setting_list.html", context)
#
#
# def setting_view(request, id):
#     context = {'setting_view': Setting.objects.get(pk=id)}
#     return render(request, "setting/setting_view", context)


def setting_create(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = SettingForm()
        else:
            setting = get_object_or_404(Setting, pk=id)
            form = SettingForm(instance=setting)
        return render(request, "setting/setting_create.html", {'form': form})
    else:
        if request.method == "POST":
            if id == 0:
                form = SettingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/setting/list')

#
# def setting_update(request, id):
#     setting = get_object_or_404(Setting, pk=id)
#     form = SettingForm(instance=setting)
#
#     if request.method == 'POST':
#         form = SettingForm(request.POST, instance=setting)
#         if form.is_valid():
#             form.save()
#             return redirect('/setting/list')
#
#     context = {'form': form}
#     return render(request, 'setting/setting_update.html', context)
#
#
# def setting_delete(request, id):
#     setting = get_object_or_404(Setting, pk=id)
#     setting.delete()
#     return redirect('/setting/list')


# Buyer
def buyer_list(request):
    context = {'buyer_list': Buyer.objects.all()}
    return render(request, "buyer/buyer_list.html", context)


def buyer_view(request, id):
    context = {'buyer_view': Buyer.objects.get(pk=id)}
    return render(request, "buyer/buyer_view", context)


def buyer_create(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BuyerForm()
        else:
            buyer = get_object_or_404(Buyer, pk=id)
            form = BuyerForm(instance=buyer)
        return render(request, "buyer/buyer_create.html", {'form': form})
    else:
        if request.method == "POST":
            if id == 0:
                form = BuyerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/buyer/list')


def buyer_update(request, id):
    buyer = get_object_or_404(Buyer, pk=id)
    form = BuyerForm(instance=buyer)

    if request.method == 'POST':
        form = BuyerForm(request.POST, instance=buyer)
        if form.is_valid():
            form.save()
            return redirect('/buyer/list')

    context = {'form': form}
    return render(request, 'buyer/buyer_update.html', context)


def buyer_delete(request, id):
    buyer = get_object_or_404(Buyer, pk=id)
    buyer.delete()
    return redirect('/buyer/list')


# Invoice
def invoice_list(request):
    context = {'invoice_list': Invoice.objects.all()}
    return render(request, "invoice/invoice_list.html", context)


def invoice_view(request, id):
    context = {'invoice_view': Invoice.objects.get(pk=id)}
    return render(request, "invoice/invoice_view", context)


def invoice_create(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = InvoiceForm()
        else:
            invoice = get_object_or_404(Invoice, pk=id)
            form = InvoiceForm(instance=invoice)
        return render(request, "invoice/invoice_create.html", {'form': form})
    else:
        if request.method == "POST":
            if id == 0:
                form = InvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/invoice/list')


def invoice_update(request, id):
    invoice = get_object_or_404(Invoice, pk=id)
    form = InvoiceForm(instance=invoice)

    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('/invoice/list')

    context = {'form': form}
    return render(request, 'invoice/invoice_update.html', context)


def invoice_delete(request, id):
    invoice = get_object_or_404(Invoice, pk=id)
    invoice.delete()
    return redirect('/invoice/list')


# Product
def product_list(request):
    context = {'product_list': Product.objects.all()}
    return render(request, "product/product_list.html", context)


def product_view(request, id):
    context = {'product_view': Product.objects.get(pk=id)}
    return render(request, "product/product_view", context)


def product_create(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            product = get_object_or_404(Product, pk=id)
            form = ProductForm(instance=product)
        return render(request, "product/product_create.html", {'form': form})
    else:
        if request.method == "POST":
            if id == 0:
                form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/product/list')


def product_update(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/product/list')

    context = {'form': form}
    return render(request, 'product/product_update.html', context)


def product_delete(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('/product/list')


# Pos
def pos_list(request):
    context = {'pos_list': Pos.objects.all()}
    return render(request, "pos/pos_list.html", context)


def pos_view(request, id):
    context = {'pos_view': Pos.objects.get(pk=id)}
    return render(request, "pos/pos_view", context)


def pos_create(request, id=0):
    if request.method == "GET":
        setting_data = get_object_or_404(Setting, id=1)

        if id == 0:
            form = PosForm()
        else:
            pos = get_object_or_404(Pos, pk=id)

            form = PosForm(instance=pos)
        return render(request, "pos/pos_create.html", {'form': form, 'setting_data': setting_data})
    else:
        if request.method == "POST":
            if id == 0:
                form = PosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/pos/list')


def pos_update(request, id):
    pos = get_object_or_404(Pos, pk=id)
    form = PosForm(instance=pos)

    if request.method == 'POST':
        form = PosForm(request.POST, instance=pos)
        if form.is_valid():
            form.save()
            return redirect('/pos/list')

    context = {'form': form}
    return render(request, 'pos/pos_update.html', context)


def pos_delete(request, id):
    pos = get_object_or_404(Pos, pk=id)
    pos.delete()
    return redirect('/pos/list')

#
# def pos_seller_create(request, id):
#     setting_data = Setting.objects.get(id=1)
#     form = PosForm()
#
#     if request.method == 'POST':
#         form = PosForm(request.POST, request.FILES, initial={'setting_data': setting_data})
#         if form.is_valid():
#             setting = Setting.objects.get(id=1)
#             obj = form.save(commit=False)
#             obj.setting = setting
#             obj.save()
#
#         return redirect('/pos/list')
#     context = {'form': form, 'setting_data': setting_data}
#     return render(request, 'pos/pos_create.html', context)


def pos_buyer_create(request, id):
    buyer_data = Buyer.objects.get(id=id)
    form = PosForm()

    if request.method == 'POST':
        form = PosForm(request.POST, request.FILES, initial={'buyer_data': buyer_data})
        if form.is_valid():
            buyer = Buyer.objects.get(pk=id)
            obj = form.save(commit=False)
            obj.buyer = buyer
            obj.save()

        return redirect('/pos/list')
    context = {'form': form, 'buyer_data': buyer_data}
    return render(request, 'pos/pos_create.html', context)


def pos_product_create(request, id):
    product_data = Product.objects.get(id=id)
    form = PosForm(instance=product_data)

    if request.method == 'POST':
        form = PosForm(request.POST, request.FILES, initial={'product_data': product_data})
        if form.is_valid():
            product = Product.objects.get(pk=id)
            obj = form.save(commit=False)
            obj.product = product
            obj.save()

        return redirect('/pos/list')
    context = {'form': form, 'product_data': product_data}
    return render(request, 'pos/pos_create.html', context)
