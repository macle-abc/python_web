from rest_framework import generics

from .models import HomeEncyclopedias
from .serializers import HomeEncyclopediasSerializer


class HomeEncyclopediasListView(generics.ListAPIView):
    queryset = HomeEncyclopedias.objects.all()
    serializer_class = HomeEncyclopediasSerializer


class HomeEncyclopediasDetailView(generics.RetrieveAPIView):
    queryset = HomeEncyclopedias.objects.all()
    serializer_class = HomeEncyclopediasSerializer
