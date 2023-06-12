from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (SerializerMethodField)
from Producto.models import Producto

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
