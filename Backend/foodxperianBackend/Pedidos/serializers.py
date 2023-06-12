from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (SerializerMethodField)
from Pedidos.models import Pedido

class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
