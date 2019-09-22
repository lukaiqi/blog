from rest_framework import serializers
from .models import Jinghua


class DakaListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jinghua
        fields = '__all__'
