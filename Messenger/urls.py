from django.urls import path
from django.views.generic import TemplateView
from Messenger import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='chat.html'), name='home'),
    # Api:
    path('api/message/', views.MessageList.as_view(), name='MessageList'),
    path('api/message/<int:message_id>/', views.MessageDetails.as_view(), name='MessageDetails'),
    path('api/users/', views.UserList.as_view(), name='UserList'),
    path('api/user/<int:user_id>/', views.UserDetails.as_view(), name='UserDetails')
]
