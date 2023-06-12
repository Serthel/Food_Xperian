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
from RegistrosMensajes.serializers import RegistroMensajeSerializer
from RegistrosMensajes.models import RegistroMensaje
# Create your views here.

# Vistas de MVT

class RegistroMensajeListView(ListView):
    model = RegistroMensaje
    template_name = 'RegistroMensaje_list.html'
    context_object_name = 'object_list'

# Vistas de Api

@permission_classes((AllowAny, ))
class RegistroMensajeListApi(ListAPIView):
    serializer_class = RegistroMensajeSerializer
    queryset = RegistroMensaje.objects.all().order_by('id')


@permission_classes((AllowAny,))
class RegistroMensajeSerializer(CreateAPIView):
    queryset = RegistroMensaje.objects.all()
    serializer_class = RegistroMensajeSerializer
