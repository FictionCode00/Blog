from rest_framework import serializers
from .models import Category, blog


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model= blog
        fields="__all__"        