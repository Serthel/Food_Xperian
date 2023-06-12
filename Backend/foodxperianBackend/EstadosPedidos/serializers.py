from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (SerializerMethodField)
from EstadosPedidos.models import EstadoPedido

class EstadoPedidoSerializer(ModelSerializer):
    class Meta:
        model = EstadoPedido
        fields = '__all__'
