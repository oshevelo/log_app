from django.urls import path, include
from . import views
from .views import RegisterAPI, LoginAPI, ChangePasswordView
from knox import views as knox_views
from django.contrib.auth import logout


app_name = "accounts"


urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name='login'),
    path('', logout, name='home'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
]