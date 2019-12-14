import random

from django.forms import model_to_dict
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from girl.models import Music, Sentence
from girl.serializers import MusicListSerializer, SentenceListSerializer


class MusicListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Music.objects.all().order_by('-id')
    serializer_class = MusicListSerializer
