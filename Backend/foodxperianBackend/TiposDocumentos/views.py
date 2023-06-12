from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    DestroyAPIView)
    # GenericAPIView
from django.urls import reverse_lazy
from TiposDocumentos.serializers import TipoDocumentoSerializer
from TiposDocumentos.models import TipoDocumento

# Create your views here.

# Vistas de MVT

class TipoDocumentoListView(ListView):
    model = TipoDocumento
    template_name = 'TipoDocumento_list.html'
    context_object_name = 'object_list'

# Vistas de Api

@permission_classes((AllowAny, ))
class TipoDocumentoListApi(ListAPIView):
    serializer_class = TipoDocumentoSerializer
    queryset = TipoDocumento.objects.all().order_by('id')
