from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    """
    访客IP
    """

    class Meta:
        model = Client
        fields = '__all__'
