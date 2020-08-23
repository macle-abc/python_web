from rest_framework import generics

from .models import CustomerCases, CustomerCasesImages, CustomerCasesVideos
from .serializers import CustomerCasesSerializer, CustomerCasesImagesSerializer, CustomerCasesVideosSerializer


class CustomerCasesVideosListView(generics.ListAPIView):
    queryset = CustomerCasesVideos.objects.all()
    serializer_class = CustomerCasesVideosSerializer


class CustomerCasesVideosDetailView(generics.RetrieveAPIView):
    queryset = CustomerCasesVideos.objects.all()
    serializer_class = CustomerCasesVideosSerializer


class CustomerCasesImagesListView(generics.ListAPIView):
    queryset = CustomerCasesImages.objects.all()
    serializer_class = CustomerCasesImagesSerializer


class CustomerCasesListView(generics.ListAPIView):
    queryset = CustomerCases.objects.all()
    serializer_class = CustomerCasesSerializer


class CustomerCasesImagesDetailView(generics.RetrieveAPIView):
    queryset = CustomerCasesImages.objects.all()
    serializer_class = CustomerCasesImagesSerializer


class CustomerCasesDetailView(generics.RetrieveAPIView):
    queryset = CustomerCases.objects.all()
    serializer_class = CustomerCasesSerializer
