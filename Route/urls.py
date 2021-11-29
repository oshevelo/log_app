from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('route/', views.RouteList.as_view(), name='RouteList')
]
