import random
from django.shortcuts import render, redirect
from .models import CatImage, DogImage
from .serializers import CatImageSerializer, DogImageSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'home.html')

def endpoints(request):
    return render(request, 'endpoints.html')

def documentation(request):
    return render(request, 'documentation.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Incorrect credentials.')
            return render(request, 'login.html')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created succesfully.')
            return redirect('login')

    context = {'form':form}
    return render(request, 'register.html', context)

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