from django.urls import path

from . import views

urlpatterns = [
    path('', views.QuestionList.as_view(), name='QuestionList'),
    path('<int:question_id>/', views.QuestionDetails.as_view(), name='QuestionDetails')
]
