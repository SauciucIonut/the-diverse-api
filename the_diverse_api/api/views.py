import random
from django.shortcuts import render
from .models import Cats
from .serializers import CatsSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def cats(request):
    if request.method == 'GET':
        # getting a random cat, serializing it then responding to
        # the api call, might make it a one-liner in the future
        cats = random.choice(list(Cats.objects.all()))
        return Response(CatsSerializer(cats).data)

    elif request.method == 'POST':
        serializer = CatsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)