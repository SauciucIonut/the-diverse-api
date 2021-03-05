from rest_framework import serializers
from .models import CatImage, DogImage


class CatImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatImage
        fields = ["id", "link"]


class DogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogImage
        fields = ["id", "link"]
