"""Serializers"""

from rest_framework import serializers

from .models import Room


class Roomserializer(serializers.ModelSerializer):
    """Serializer for the room model"""

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
