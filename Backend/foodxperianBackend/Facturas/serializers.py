from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (SerializerMethodField)
from Facturas.models import Factura

class FacturaSerializer(ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'
