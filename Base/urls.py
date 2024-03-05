from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="Home"),
    path('room/<str:pk>/',views.room, name = "room"),
    path('create-room/',views.CreateRoom, name = "Create-Room"),
    path('update-room/<str:pk>/',views.updateRoom, name = "update-Room"),
    path('delete-room/<str:pk>/',views.deleteRoom, name = "delete-Room"),
    path('room/<str:pk>/add-message/',views.CreateMessage,name='Create-message')
    
]