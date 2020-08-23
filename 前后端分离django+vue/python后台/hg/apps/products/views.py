from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .models import Products, ProductsImages
from .serializers import ProductsSerializer, ProductsImagesSerializer


class ProductsListView(generics.ListAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
# class ProductsListView(APIView):
#     def get(self, request, format=None):
#         get_dict = request.GET
#         if get_dict:
#             if 'category' in get_dict:
#                 queryset = Products.objects.filter(classification=get_dict['category'])
#                 if queryset:
#                     serializer = ProductsSerializer(queryset, many=True, context={"request": request})
#                     return Response(serializer.data)
#                 else:
#                     return Response([], status=status.HTTP_204_NO_CONTENT)
#             else:
#                 return Response([], status=status.HTTP_400_BAD_REQUEST)
#         else:
#             queryset = Products.objects.all()
#             serializer = ProductsSerializer(queryset, many=True, context={"request": request})
#             return Response(serializer.data)


class ProductsDetailView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


def get_display_name(classification):
    for item in Products.CLASSIFICATION_CHOICES:
        if item[0] == classification:
            return item[1]
    else:
        return ""


class ProductsImagesDetailView(generics.RetrieveAPIView):
    serializer_class = ProductsImagesSerializer
    queryset = ProductsImages

#
# class ProductsImagesListView(generics.ListAPIView):
#     serializer_class = ProductsImagesSerializer
#     queryset = ProductsImages

# class ProductsCategoriesView(APIView):
#     def get(self, request, format=None):
#         queryset = Products.objects.values("classification")
#         result = set(
#             [
#                 (
#                     item['classification'],
#                     "{url}?{query}".format(
#                         url=reverse("products:products-list",
#                                     request=request,
#                                     format=format),
#                         query=f"category={item['classification']}"
#                     )
#                 )
#                 for item in queryset
#             ]
#         )
#         if result:
#             result = [
#                 {
#                     "classification": get_display_name(item[0]),
#                     "url": item[1]
#                 }
#                 for item in result
#             ]
#             return Response(result)
#         else:
#             return Response([], status=status.HTTP_204_NO_CONTENT)
