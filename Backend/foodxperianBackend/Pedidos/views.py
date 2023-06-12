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
from Pedidos.serializers import PedidoSerializer
from Pedidos.models import Pedido

# Create your views here.

# Vistas de MVT

class PedidoListView(ListView):
    model = Pedido
    template_name = 'Pedido_list.html'
    context_object_name = 'object_list'

# Vistas de Api

@permission_classes((AllowAny, ))
class PedidoListApi(ListAPIView):
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all().order_by('id')
