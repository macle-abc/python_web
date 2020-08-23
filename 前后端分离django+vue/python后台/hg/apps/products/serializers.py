from rest_framework import serializers

from .models import Products, ProductsImages


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="products:products-detail")
    products_images = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="products:products_images-detail"
    )

    class Meta:
        model = Products
        fields = [
            'url',
            'name',
            'style',
            'site',
            'feature',
            'key_word',
            'cover',
            'products_images',
        ]


class ProductsImagesSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="products:products_images-detail")

    class Meta:
        model = ProductsImages
        fields = [
            'url',
            'image',
        ]
