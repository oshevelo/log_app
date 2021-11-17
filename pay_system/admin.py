from django.contrib import admin
from .models import pay_check
# Register your models here.

@admin.register(pay_check)
class pay_check(admin.ModelAdmin):
    list_display = ["pk", 'pay_time', 'payer', "sum", "email" ]

