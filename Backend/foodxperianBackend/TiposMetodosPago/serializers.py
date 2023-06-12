from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (SerializerMethodField)
from TiposMetodosPago.models import TipoMetodoPago

class TipoMetodoPagoSerializer(ModelSerializer):
    class Meta:
        model = TipoMetodoPago
        fields = '__all__'
