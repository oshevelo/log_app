from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView

from .import views


urlpatterns = [

    path('all/', views.PricePlanList.as_view(), name='all'),
    path('<int:pay_id>/', views.PayDetails.as_view(), name='PayDetails'),
    path('BasePay/' ,views.BasePlan),
    path('ProPay/' ,views.ProPlan),
    path('VipPay/' ,views.VipPlan),
]