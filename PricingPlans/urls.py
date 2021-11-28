from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView

from .import views

urlpatterns = [

    path('basic/', views.PricePlanList.as_view(), name='basic'),
    url("pays/", views.process_payment, name="pay")
    # path('<int:pk>/', views.PayDetails.as_view(), name='PaysDetails')
]