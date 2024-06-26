"""Views"""

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Room
from .serializers import CreateRoomSerializer, Roomserializer


# A view to return all the rooms
class RoomView(generics.CreateAPIView):
    """View for the room model"""

    queryset = Room.objects.all()
    serializer_class = Roomserializer


class CreateRoomView(APIView):
    """View for when you want to create a new room"""

    serializer_class = CreateRoomSerializer

    # pylint:disable=redefined-builtin, unused-argument
    def post(self, request, format=None):
        """Define what happens with post?"""
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get("guest_can_pause")
            votes_to_skip = serializer.data.get("votes_to_skip")
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=["guest_can_pause", "votes_to_skip"])
                return Response(Roomserializer(room).data, status=status.HTTP_200_OK)

            room = Room(
                host=host,
                guest_can_pause=guest_can_pause,
                votes_to_skip=votes_to_skip,
            )
            room.save()
            return Response(Roomserializer(room).data, status=status.HTTP_201_CREATED)

        return Response(
            {"Bad Request": "Invalid data..."}, status=status.HTTP_400_BAD_REQUEST
        )
