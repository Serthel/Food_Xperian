from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (SerializerMethodField)
from DatosDomicilio.models import DatoDomicilio



class DatoDomicilioSerializer(ModelSerializer):
    class Meta:
        model = DatoDomicilio
        fields = '__all__'

