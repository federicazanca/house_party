"""Store urls local to this app"""

from django.urls import path

from .views import CreateRoomView, RoomView

# Admin is already defined, the rest we are defining

urlpatterns = [
    path("room", RoomView.as_view()),
    path("create-room", CreateRoomView.as_view()),
]
