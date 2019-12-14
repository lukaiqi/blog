from rest_framework import serializers
from .models import Music, Sentence


class MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'


class SentenceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = '__all__'
