from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (SerializerMethodField)
from Notificaciones.models import Notificacion

class NotificacionSerializer(ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'
