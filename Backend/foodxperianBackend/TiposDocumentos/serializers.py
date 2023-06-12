from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (SerializerMethodField)
from TiposDocumentos.models import TipoDocumento

class TipoDocumentoSerializer(ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'

