import requests
from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView
from .import views
from .forms import *
from .models import PricePlan


urlpatterns = [

    path('all/', views.PricePlanList.as_view(), name='all'),
    path('<int:pay_id>/', views.PayDetails.as_view(), name='PayDetails'),
    path('Pay/' ,views.choicen_plan),
    path('', views.testy, name="testy")
]