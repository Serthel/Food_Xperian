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
from TiposMetodosPago.serializers import TipoMetodoPagoSerializer
from TiposMetodosPago.models import TipoMetodoPago


# Create your views here.

# Vistas de MVT

class TipoMetodoPagoListView(ListView):
    model = TipoMetodoPago
    template_name = 'TipoMetodoPago_list.html'
    context_object_name = 'object_list'

# Vistas de Api

@permission_classes((AllowAny, ))
class TipoMetodoPagoListApi(ListAPIView):
    serializer_class = TipoMetodoPagoSerializer
    queryset = TipoMetodoPago.objects.all().order_by('id')

