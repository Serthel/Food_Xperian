from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (SerializerMethodField)
from EstadosEntrega.models import EstadoEntrega

class EstadoEntregaSerializer(ModelSerializer):
    class Meta:
        model = EstadoEntrega
        fields = '__all__'

