from rest_framework import serializers

from .models import HomeEncyclopedias


class HomeEncyclopediasSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="home_encyclopedias:home_encyclopedias-detail")

    class Meta:
        model = HomeEncyclopedias
        fields = [
           'url',
           'create_time',
           'problem',
           'answer',
        ]
