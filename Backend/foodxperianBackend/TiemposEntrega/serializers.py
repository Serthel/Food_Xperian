from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (SerializerMethodField)
from TiemposEntrega.models import TiempoEntrega

class TiempoEntregaSerializer(ModelSerializer):
    class Meta:
        model = TiempoEntrega
        fields = '__all__'
