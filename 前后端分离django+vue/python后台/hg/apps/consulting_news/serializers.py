from rest_framework import serializers

from .models import ConsultingNews


class ConsultingNewsSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="consulting_news:consulting_news-detail")

    class Meta:
        model = ConsultingNews
        fields = [
            'url',
            'title',
            'content',
            'release_time',
        ]
