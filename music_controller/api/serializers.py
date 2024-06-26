"""Serializers"""

from rest_framework import serializers

from .models import Room


class Roomserializer(serializers.ModelSerializer):
    """Serializer for the room model. Take a room object and serialize into something
    we can return back as a response"""

    class Meta:
        """Meta"""

        model = Room
        fields = (
            "id",
            "code",
            "host",
            "guest_can_pause",
            "votes_to_skip",
            "created_at",
        )


class CreateRoomSerializer(serializers.ModelSerializer):
    """Make sure the data sent to the request is valid and give it back in a python
    format. Serialize a request"""

    class Meta:
        """Meta"""

        model = Room
        fields = ("guest_can_pause", "votes_to_skip")
