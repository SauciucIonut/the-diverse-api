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
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
from .throttles import FreeUserThrottle, PremiumUserThrottle, SubscriptionRateThrottle
from ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

# API ENDPOINTS ----------------------------------------------------------------------------


class CatImagesLink(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    throttle_classes = [SubscriptionRateThrottle]
    serializer_class = CatImageSerializer

    @method_decorator(ratelimit(key="ip", rate="61/60s", method="GET", block=True))
    def get(self, request):
        return Response(
            CatImageSerializer(
                random.choice(list(CatImage.objects.all())), many=False
            ).data
        )

    def post(self, request):
        # don't accept any post requests for now
        return Response(
            {"error": "not accepting POSTs for now"}, status=status.HTTP_400_BAD_REQUEST
        )
        serializer = CatImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogImagesLink(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    throttle_classes = [SubscriptionRateThrottle]
    serializer_class = DogImageSerializer

    @method_decorator(ratelimit(key="ip", rate="60/60s", method="GET", block=True))
    def get(self, request):
        return Response(
            DogImageSerializer(
                random.choice(list(DogImage.objects.all())), many=False
            ).data
        )

    def post(self, request):
        # don't accept any post requests for now
        return Response(
            {"error": "not accepting POSTs for now"}, status=status.HTTP_400_BAD_REQUEST
        )
        serializer = DogImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# USER LOGIN LOGOUT REGISTER ---------------------------------------------------------------


@ratelimit(key="ip", rate="5/m", method=["GET", "POST"], block=True)
def loginpage(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.info(request, "Incorrect credentials.")
            return render(request, "login.html")
    context = {}
    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


@ratelimit(key="ip", rate="5/m", method=["GET", "POST"], block=True)
def register(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account was created succesfully.")
            return redirect("login")

    context = {"form": form}
    return render(request, "register.html", context)


# FRONT-END -------------------------------------------------------------------------------


def home(request):
    return render(request, "home.html")


def documentation(request):
    return render(request, "documentation/welcome.html")


def documentationanimals(request):
    return render(request, "documentation/animals.html")


def documentationexamples(request):
    return render(request, "documentation/examples.html")


def tokenpage(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(
        request,
        "token.html",
        {"token": Token.objects.get(user=request.user).key, "title": "TDA Token"},
    )
