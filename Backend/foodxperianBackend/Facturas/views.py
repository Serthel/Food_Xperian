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
from Facturas.serializers import FacturaSerializer
from Facturas.models import Factura

# Create your views here.

# Vistas de MVT

class FacturaListView(ListView):
    model = Factura
    template_name = 'Factura_list.html'
    context_object_name = 'object_list'

# Vistas de Api

@permission_classes((AllowAny, ))
class FacturaListApi(ListAPIView):
    serializer_class = FacturaSerializer
    queryset = Factura.objects.all().order_by('id')
