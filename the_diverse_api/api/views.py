import random
from django.shortcuts import render
from .models import CatImage, DogImage
from .serializers import CatImageSerializer, DogImageSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Create your views here.

def home(request):
    return render(request, 'home.html')

def endpoints(request):
    return render(request, 'endpoints.html')

def documentation(request):
    return render(request, 'documentation.html')

def login(request):
    return render(request, 'login.html')

class CatImagesLink(generics.ListCreateAPIView):
    serializer_class = CatImageSerializer
    def get(self, request):
        return Response(CatImageSerializer(random.choice(list(CatImage.objects.all())), many=False).data)

    def post(self, request):
        # don't accept any post requests for now
        return Response({'error':'not accepting POSTs for now'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CatImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DogImagesLink(generics.ListCreateAPIView):
    serializer_class = CatImageSerializer
    def get(self, request):
        return Response(DogImageSerializer(random.choice(list(DogImage.objects.all())), many=False).data)

    def post(self, request):
        # don't accept any post requests for now
        return Response({'error':'not accepting POSTs for now'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = DogImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)