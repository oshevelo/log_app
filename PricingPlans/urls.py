from django.urls import path

from .import views

urlpatterns = [
    # ex: /polls/
    path('basic/', views.BasicPlanList.as_view(), name='basic'),
    path('pro/', views.ProPlanList.as_view(), name='pro'),
    path('vip/', views.VipPlanList.as_view(), name='vip'),
    # path('<int:pk>/', views.PayDetails.as_view(), name='PaysDetails')
]