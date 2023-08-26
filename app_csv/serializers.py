
from rest_framework import serializers

from app_csv.models import Client, ListNameStone


class ListNameStoneSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = ListNameStone
        fields = ["name"]


class ClientSerializer(serializers.ModelSerializer):
    gems = ListNameStoneSerializer(many=True)

    class Meta:
        model = Client
        fields = "__all__"
