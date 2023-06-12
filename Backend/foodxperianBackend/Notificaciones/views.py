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
from Notificaciones.serializers import NotificacionSerializer
from Notificaciones.models import Notificacion


# Create your views here.

# Vistas de MVT

class NotificacionListView(ListView):
    model = Notificacion
    template_name = 'Notificacion_list.html'
    context_object_name = 'object_list'

# Vistas de Api

@permission_classes((AllowAny, ))
class NotificacionListApi(ListAPIView):
    serializer_class = NotificacionSerializer
    queryset = Notificacion.objects.all().order_by('id')
