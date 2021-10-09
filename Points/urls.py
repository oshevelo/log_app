from django.urls import path
from . import views

app_name = "Points"


urlpatterns = [
    path("signup/", views.signup, name="signup")
]