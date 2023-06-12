from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (SerializerMethodField)
from  RegistrosMensajes.models import RegistroMensaje

class RegistroMensajeSerializer(ModelSerializer):
    class Meta:
        model = RegistroMensaje
        fields = '__all__'