from rest_framework import serializers
from news.models import Headline

class HeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headline
        fields = ['title', 'contentt']


class HeadlineTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headline
        fields = ['title']
