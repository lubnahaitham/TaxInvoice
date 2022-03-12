from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Setting)
admin.site.register(Buyer)
admin.site.register(Invoice)
admin.site.register(Product)
admin.site.register(Pos)
admin.site.register(CloseInvoice)