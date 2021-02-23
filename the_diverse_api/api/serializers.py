from rest_framework import serializers
from .models import Cats

class CatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cats
        fields = ['id', 'link']