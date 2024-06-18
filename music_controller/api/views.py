"""Views"""

from django.shortcuts import render
from rest_framework import generics

from .models import Room
from .serializers import Roomserializer


# A view to return all the rooms
class RoomView(generics.CreateAPIView):
    """View for the room model"""

    queryset = Room.objects.all()
    serializer_class = Roomserializer
