from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.PaysList.as_view(), name='index'),
    path('<int:pk>/', views.PaysDetails.as_view(), name='PaysDetails')
]
