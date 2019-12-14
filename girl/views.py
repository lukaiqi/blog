from rest_framework import mixins, viewsets

from girl.models import Music, Sentence
from girl.serializers import MusicListSerializer, SentenceListSerializer


class MusicListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Music.objects.all().order_by('-id')
    serializer_class = MusicListSerializer


class SentenceListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Sentence.objects.all().order_by('-id')
    serializer_class = SentenceListSerializer
