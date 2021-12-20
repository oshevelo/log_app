from django.urls import path

from .views import OrderList, OrderDetail, OrderItemCreate


urlpatterns = [
    path('list/', OrderList.as_view(), name='OrderList'),
    path('<int:order_id>/', OrderDetail.as_view(), name='OrderDetail'),
    path('<int:order_id>/items/', OrderItemCreate.as_view(), name='OrderItemCreate'),
]
