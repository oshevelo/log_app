from django.contrib import admin
from .models import BasicPlan, ProPlan, VipPlan
# Register your models here.

@admin.register(BasicPlan)
class BasicPlan(admin.ModelAdmin):
    list_display = ["pk", 'payment_time', 'payer', "plan_cost"]

@admin.register(ProPlan)
class ProPlan(admin.ModelAdmin):
    list_display = ["pk", 'payment_time', 'payer', "plan_cost"]

@admin.register(VipPlan)
class VipPlan(admin.ModelAdmin):
    list_display = ["pk", 'payment_time', 'payer', "plan_cost"]