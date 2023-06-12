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
from Producto.serializers import ProductoSerializer
from Producto.models import Producto

# Create your views here.

# Vistas de MVT

class ProductoListView(ListView):
    model = Producto
    template_name = 'Producto_list.html'
    context_object_name = 'object_list'

# Vistas de Api

@permission_classes((AllowAny, ))
class ProductoListApi(ListAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all().order_by('id')

@permission_classes((AllowAny,))
class ProductoSerializer(CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer