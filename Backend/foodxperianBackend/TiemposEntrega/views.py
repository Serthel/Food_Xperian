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
from TiemposEntrega.serializers import TiempoEntregaSerializer
from TiemposEntrega.models import TiempoEntrega
# Create your views here.

# Vistas de MVT

class TiempoEntregaListView(ListView):
    model = TiempoEntrega
    template_name = 'TiempoEntrega_list.html'
    context_object_name = 'object_list'

# Vistas de Api

@permission_classes((AllowAny, ))
class TiempoEntregaListApi(ListAPIView):
    serializer_class = TiempoEntregaSerializer
    queryset = TiempoEntrega.objects.all().order_by('id')
