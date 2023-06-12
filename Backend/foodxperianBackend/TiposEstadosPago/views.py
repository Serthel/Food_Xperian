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
from TiposEstadosPago.serializers import TipoEstadoPagoSerializer
from TiposEstadosPago.models import TipoEstadoPago

# Create your views here.

# Vistas de MVT

class TiposEstadosPagoListView(ListView):
    model = TipoEstadoPago
    template_name = 'TipoEstadoPago_list.html'
    context_object_name = 'object_list'

# Vistas de Api

@permission_classes((AllowAny, ))
class TipoEstadoPagoListApi(ListAPIView):
    serializer_class = TipoEstadoPagoSerializer
    queryset = TipoEstadoPago.objects.all().order_by('id')
