from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.http import require_http_methods

from .decorators import unauthenticated_user
from .forms import SettingForm, ProductForm, PosForm, CreateUserForm, InvoiceForm, BuyerForm
from .models import Setting, Buyer, Invoice, Product, Pos


# Create your views here.

def home(request):
    return render(request, 'homepage.html')


@unauthenticated_user
# @admin_only
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('/login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/login')


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
        return redirect('/invoice/list')


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
# def buyer_list(request):
#     context = {'buyer_list': Buyer.objects.all()}
#     return render(request, "buyer/buyer_list.html", context)
#
#
# def buyer_view(request, id):
#     context = {'buyer_view': Buyer.objects.get(pk=id)}
#     return render(request, "buyer/buyer_view", context)
#
#
# def buyer_create(request, id=0):
#     if request.method == "GET":
#         if id == 0:
#             form = BuyerForm()
#         else:
#             buyer = get_object_or_404(Buyer, pk=id)
#             form = BuyerForm(instance=buyer)
#         return render(request, "buyer/buyer_create.html", {'form': form})
#     else:
#         if request.method == "POST":
#             if id == 0:
#                 form = BuyerForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#         return redirect('/buyer/list')
#
#
# def buyer_update(request, id):
#     buyer = get_object_or_404(Buyer, pk=id)
#     form = BuyerForm(instance=buyer)
#
#     if request.method == 'POST':
#         form = BuyerForm(request.POST, instance=buyer)
#         if form.is_valid():
#             form.save()
#             return redirect('/buyer/list')
#
#     context = {'form': form}
#     return render(request, 'buyer/buyer_update.html', context)
#
#
# def buyer_delete(request, id):
#     buyer = get_object_or_404(Buyer, pk=id)
#     buyer.delete()
#     return redirect('/buyer/list')


# Invoice
# def invoice_list(request):
#     invoice_list = Invoice.objects.all()
#
#     context = {'invoice_list': invoice_list}
#     return render(request, "pos/pos_list.html", context)
#
#
# def invoice_view(request, id):
#     invoice_data = Invoice.objects.get(pk=id)
#     context = {'invoice_data': invoice_data}
#     return render(request, "invoice/invoice_view.html", context)


# def invoice_create(request, id=0):
#     if request.method == "GET":
#         if id == 0:
#             form = InvoiceForm()
#         else:
#             invoice = get_object_or_404(Invoice, pk=id)
#             form = InvoiceForm(instance=invoice)
#         return render(request, "invoice/invoice_create.html", {'form': form})
#     else:
#         if request.method == "POST":
#             if id == 0:
#                 form = InvoiceForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#         return redirect('/invoice/list')


#
# def invoice_update(request, id):
#     invoice = get_object_or_404(Invoice, pk=id)
#     form = InvoiceForm(instance=invoice)
#
#     if request.method == 'POST':
#         form = InvoiceForm(request.POST, instance=invoice)
#         if form.is_valid():
#             form.save()
#             return redirect('/invoice/list')
#
#     context = {'form': form}
#     return render(request, 'invoice/invoice_update.html', context)


# def invoice_delete(request, id):
#     invoice = get_object_or_404(Invoice, pk=id)
#     invoice.delete()
#     return redirect('/invoice/list')


# Product
def product_list(request):
    context = {'product_list': Product.objects.all()}
    return render(request, "product/product_list.html", context)


def product_view(request, id):
    context = {'product_view': Product.objects.get(pk=id)}
    return render(request, "product/product_view.html", context)


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
def invoice_pos_list(request):
    pos_list = Pos.objects.all()
    invoice_list = Invoice.objects.all()
    buyer_list = Buyer.objects.all()
    attribute_values = zip(invoice_list, pos_list, buyer_list)
    context = {'attribute_values': attribute_values}
    return render(request, "pos/pos_list.html", context)


def pos_view(request, id):
    pos_view = Pos.objects.get(pk=id)
    invoice_data = Invoice.objects.get(pk=id)
    buyer_data = Buyer.objects.get(id=id)
    context = {'pos_view': pos_view, 'setting_data_view': Setting.objects.get(id=1),
               'invoice_data': invoice_data, 'buyer_data': buyer_data}
    return render(request, "pos/pos_view.html", context)


def pos_create(request):
    setting_data = Setting.objects.get(id=1)
    pos_form = PosForm(request.POST or None)
    invoice_form = InvoiceForm(request.POST or None)
    buyer_form = BuyerForm(request.POST or None)

    context = {
        "pos_form": pos_form,
        "invoice_form": invoice_form,
        "buyer_form": buyer_form,
        "setting_data": setting_data,
        # 'formset': formset

    }
    if all([pos_form.is_valid(), invoice_form.is_valid(), buyer_form.is_valid()]):
        parent = pos_form.save(commit=False)
        parent.save()

        child = invoice_form.save(commit=False)
        # parent.child = child
        child.save()
        # print("invoice_form", invoice_form.cleaned_data)
        child1 = buyer_form.save(commit=False)
        parent.child1 = child1
        child1.save()

        return redirect('/invoice/list')
    return render(request, "pos/pos_create.html", context)


# def pos_update(request, id):
#     setting_data = Setting.objects.get(id=1)
#     pos = get_object_or_404(Pos, pk=id)
#     pos_form = PosForm(instance=pos)
#     invoice = get_object_or_404(Invoice, pk=id)
#     invoice_form = InvoiceForm(instance=invoice)
#     buyer = get_object_or_404(Buyer, pk=id)
#     buyer_form = BuyerForm(instance=buyer)
#
#     if request.method == 'POST':
#         pos_form = PosForm(request.POST or None, instance=pos)
#         invoice_form = InvoiceForm(request.POST or None, instance=invoice)
#         buyer_form = BuyerForm(request.POST or None, instance=buyer)
#
#         if all([pos_form.is_valid(), invoice_form.is_valid(), buyer_form.is_valid()]):
#             parent = pos_form.save(commit=False)
#             parent.save()
#             child = invoice_form.save(commit=False)
#             parent.child = child
#             child.save()
#             child1 = buyer_form.save(commit=False)
#             parent.child1 = child1
#             child1.save()
#     context = {
#         "pos_form": pos_form,
#         "invoice_form": invoice_form,
#         "buyer_form": buyer_form,
#         "setting_data": setting_data
#     }
#     return render(request, 'pos/pos_update.html', context)


def pos_delete(request, id):
    pos = get_object_or_404(Pos, pk=id)
    pos.delete()
    return redirect('/invoice/list')

#
# def pos_product_create(request, id):
#     product_data = Product.objects.get(id=id)
#     form = PosForm(instance=product_data)
#
#     if request.method == 'POST':
#         form = PosForm(request.POST, request.FILES, initial={'product_data': product_data})
#         if form.is_valid():
#             product = Product.objects.get(pk=id)
#             obj = form.save(commit=False)
#             obj.product = product
#             obj.save()
#
#         return redirect('/pos/list')
#     context = {'form': form, 'product_data': product_data}
#     return render(request, 'pos/pos_create.html', context)

#
# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         template = get_template('pos/pos_pdf.html')
#         id = kwargs['id']
#         pos_pdf = get_object_or_404(Pos, id=self.kwargs['id'])
#         invoice_pdf = get_object_or_404(Invoice, pk=id)
#         buyer_pdf = get_object_or_404(Buyer, pk=id)
#         setting_pdf = get_object_or_404(Setting, id=1)
#         data = {
#             "pos_pdf": pos_pdf, "invoice_pdf": invoice_pdf, "buyer_pdf": buyer_pdf, "setting_pdf": setting_pdf
#         }
#         pdf = html_to_pdf('pos/pos_pdf.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')


# def pdf_generation(request, id):
#     pos_pdf = get_object_or_404(Pos, pk=id)
#     invoice_pdf = get_object_or_404(Invoice, pk=id)
#     buyer_pdf = get_object_or_404(Buyer, pk=id)
#     setting_pdf = get_object_or_404(Setting, id=1)
#     template_path = 'pos/pos_pdf.html'
#     data = {
#         "pos_pdf": pos_pdf, "invoice_pdf": invoice_pdf, "buyer_pdf": buyer_pdf, "setting_pdf": setting_pdf
#     }
#
#     response = HttpResponse(content_type='application/pdf')
#
#     response['Content-Disposition'] = 'filename="products_report.pdf"'
#
#     template = get_template(template_path)
#
#     html = template.render(data)
#
#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#         html, dest=response, encoding='UTF-8')
#     # if error then show some funy view
#     if pisa_status.err:
#         return HttpResponse(html)
#     return response


# def close_invoice(request):
#     pos = request.GET.get('pos_view')
#     if 'pos_view' in request.POST:
#         pos = request.POST['pos_view']
#
#     return render(request, 'newhome.html', {'pos': pos})
