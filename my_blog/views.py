from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer,blogSerializer
from .models import Category,blog

# Create your views here.


class CategoryAPIView(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class CategoryupanddestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer    


class blogAPIView(generics.ListCreateAPIView):
    queryset=blog.objects.all()
    serializer_class=blogSerializer    


class blogupdateanddestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=blog.objects.all()
    serializer_class=blogSerializer    