"""Store urls local to this app"""
from django.urls import path
from .views import RoomView
#Admin is already defined, the rest we are defining

urlpatterns = [
    path('home', RoomView.as_view()),
]