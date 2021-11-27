from django.contrib import admin
from .models import PayCheck
# Register your models here.

@admin.register(PayCheck)
class PayCheck(admin.ModelAdmin):
    list_display = ["pk", 'pay_time', 'payer', "sum", "email" ]