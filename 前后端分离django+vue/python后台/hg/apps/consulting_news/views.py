from rest_framework import generics

from .models import ConsultingNews
from .serializers import ConsultingNewsSerializer


class ConsultingNewsList(generics.ListAPIView):
    queryset = ConsultingNews.objects.all()
    serializer_class = ConsultingNewsSerializer


class ConsultingNewsDetail(generics.RetrieveAPIView):
    queryset = ConsultingNews.objects.all()
    serializer_class = ConsultingNewsSerializer
