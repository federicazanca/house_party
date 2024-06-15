from django.shortcuts import render
from rest_framework import generics
from .serializers import Roomserializer
from .models import Room

# A view to return all the rooms
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = Roomserializer

