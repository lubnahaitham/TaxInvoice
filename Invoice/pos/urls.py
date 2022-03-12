
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


# from .views import GeneratePdf


urlpatterns = [

   
    # Login and Register
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name='home'),
    # setting
    # path('setting/list/', views.setting_list, name='setting_list'),
    # path('setting/view/<int:id>/', views.setting_view, name='setting_view'),
    path('setting/create/', views.setting_create, name='setting_create'),
    # path('setting/update/<int:id>/', views.setting_update, name='setting_update'),
    # path('setting/delete/<int:id>/', views.setting_delete, name='setting_delete'),

    # buyer
    # path('buyer/list/', views.buyer_list, name='buyer_list'),
    # path('buyer/view/<int:id>/', views.buyer_view, name='buyer_view'),
    # path('buyer/create/', views.buyer_create, name='buyer_create'),
    # path('buyer/update/<int:id>/', views.buyer_update, name='buyer_update'),
    # path('buyer/delete/<int:id>/', views.buyer_delete, name='buyer_delete'),

    # invoice
    # path('invoice/list/', views.invoice_list, name='invoice_list'),
    # path('invoice/view/<int:id>/', views.invoice_view, name='invoice_view'),
    # path('invoice/create/', views.invoice_create, name='invoice_create'),
    # path('invoice/update/<int:id>/', views.invoice_update, name='invoice_update'),
    # path('invoice/delete/<int:id>/', views.invoice_delete, name='invoice_delete'),

    # product
    path('product/list/', views.product_list, name='product_list'),
    path('product/view/<int:id>/', views.product_view, name='product_view'),
    path('product/create/', views.product_create, name='product_create'),
    path('product/update/<int:id>/', views.product_update, name='product_update'),
    path('product/delete/<int:id>/', views.product_delete, name='product_delete'),

    # pos
    path('invoice/list/', views.invoice_pos_list, name='invoice_pos_list'),
    path('pos/create/', views.pos_create, name='pos_create'),
    # path('pos/update/<int:id>/', views.pos_update, name='pos_update'),
    path('pos/view/<int:id>/', views.pos_view, name='pos_view'),
    path('pos/delete/<int:id>/', views.pos_delete, name='pos_delete'),

    # path('pos/product/<int:id>/', views.pos_product_create, name='pos_product_create'),

    # path('pos/pdf/<int:id>/', GeneratePdf.as_view(), name='pos_pdf'),
    # path('pos/pdf/<int:id>/', views.pdf_generation, name='pos_pdf'),

    # path('close/invoice/', views.close_invoice, name='close_invoice_view'),

]

