from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.RouteList.as_view(), name='RouteList'),
    path('<int:route_id>', views.RouteDetails.as_view(), name='RouteDetails')
]
