from django.contrib import admin
from .models import PricePlan
# Register your models here.

@admin.register(PricePlan)
class BasicPlan(admin.ModelAdmin):
    list_display = ["pk", 'payment_time', 'payer', 'plan_type']