from rest_framework import serializers
from .models import Sensor


class SensorSerializer(serializers.ModelSerializer):
    """
    用户详情
    """

    class Meta:
        model = Sensor
        fields = '__all__'
