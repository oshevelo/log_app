from django.urls import path
from django.views.generic import TemplateView
from Messenger import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='chat.html'), name='home'),
    # Api:
    path('message/', views.MessageList.as_view(), name='MessageList'),
    path('users/', views.UserList.as_view(), name='UserList'),
    path('group-chat/', views.GroupChatList.as_view(), name='UserList'),
]
