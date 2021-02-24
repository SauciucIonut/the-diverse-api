from rest_framework import serializers
from .models import CatImage

class CatImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatImage
        fields = ['id', 'link']