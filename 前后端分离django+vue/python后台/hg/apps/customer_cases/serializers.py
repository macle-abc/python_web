from rest_framework import serializers

from .models import CustomerCasesImages, CustomerCases, CustomerCasesVideos


class CustomerCasesVideosSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="customer_cases:customer_cases_videos-detail")

    class Meta:
        model = CustomerCasesVideos
        fields = [
            'url',
            'video_effect',
        ]


class CustomerCasesImagesSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="customer_cases:customer_cases_images-detail")

    class Meta:
        model = CustomerCasesImages
        fields = [
            'url',
            'image',
        ]


class CustomerCasesSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="customer_cases:customer_cases-detail")
    customer_cases_images = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="customer_cases:customer_cases_images-detail"
    )
    customer_cases_videos = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="customer_cases:customer_cases_videos-detail"
    )

    class Meta:
        model = CustomerCases
        fields = [
            'url',
            'name',
            # 'video_effect',
            'customer_cases_images',
            'customer_cases_videos',
        ]

