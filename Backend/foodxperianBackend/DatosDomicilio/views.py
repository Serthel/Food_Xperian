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
from DatosDomicilio.serializers import DatoDomicilioSerializer
from DatosDomicilio.models import DatoDomicilio

# Create your views here.

# Vistas de MVT

class DatoDomicilioListView(ListView):
    model = DatoDomicilio
    template_name = 'DatoDomicilio_list.html'
    context_object_name = 'object_list'

# Vistas de Api

@permission_classes((AllowAny, ))
class DatoDomicilioListApi(ListAPIView):
    serializer_class = DatoDomicilioSerializer
    queryset = DatoDomicilio.objects.all().order_by('ciudad')
