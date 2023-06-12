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
from EstadosEntrega.serializers import EstadoEntregaSerializer
from EstadosEntrega.models import EstadoEntrega


# Create your views here.

# Vistas de MVT

class EstadoEntregaListView(ListView):
    model = EstadoEntrega
    template_name = 'EstadoEntrega_list.html'
    context_object_name = 'object_list'

# Vistas de Api

@permission_classes((AllowAny, ))
class EstadoEntregaListApi(ListAPIView):
    serializer_class = EstadoEntregaSerializer
    queryset = EstadoEntrega.objects.all().order_by('id')
