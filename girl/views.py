import random

from rest_framework import mixins, viewsets

from girl.models import Music, Sentence
from girl.serializers import MusicListSerializer, SentenceListSerializer


class MusicListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Music.objects.all().order_by('-id')
    serializer_class = MusicListSerializer


class SentenceListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = SentenceListSerializer

    def get_queryset(self):
        count = Sentence.objects.count()
        index = random.randint(1, count)
        queryset = Sentence.objects.filter(id=index)
        return queryset
