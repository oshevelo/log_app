from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:room_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:room_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:room_id>/vote/', views.vote, name='vote'),

    path('room/', views.RoomList.as_view(), name='RoomList'),
    path('room/<int:room_id>/', views.RoomDetails.as_view(), name='RoomDetails'),

    path('message/', views.MessageList.as_view(), name='MessageList'),
    path('message/<int:message_id>/', views.MessageDetails.as_view(), name='MessageDetails')
]
