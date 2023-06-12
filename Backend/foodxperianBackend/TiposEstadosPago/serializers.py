from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (SerializerMethodField)
from TiposEstadosPago.models import TipoEstadoPago

class TipoEstadoPagoSerializer(ModelSerializer):
    class Meta:
        model = TipoEstadoPago
        fields = '__all__'

