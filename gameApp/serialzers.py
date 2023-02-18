from rest_framework import serializers

from .models import GameDetails

class GameDetailsSerialzer(serializers.ModelSerializer):
    class Meta:
        model = GameDetails
        fields = "__all__"