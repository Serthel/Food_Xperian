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
from EstadosPedidos.serializers import EstadoPedidoSerializer
from EstadosPedidos.models import EstadoPedido

# Create your views here.

# Vistas de MVT

class EstadoPedidoListView(ListView):
    model = EstadoPedido
    template_name = 'EstadoPedido_list.html'
    context_object_name = 'object_list'

# Vistas de Api

@permission_classes((AllowAny, ))
class EstadoPedidoListApi(ListAPIView):
    serializer_class = EstadoPedidoSerializer
    queryset = EstadoPedido.objects.all().order_by('id')