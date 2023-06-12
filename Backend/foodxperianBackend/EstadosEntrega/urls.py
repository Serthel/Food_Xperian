from django.urls import path
from django.urls import re_path
from EstadosEntrega.views import EstadoEntregaListView
from .views import EstadoEntregaListApi

urlpatterns = [
    path("EstadoEntregaListView/", EstadoEntregaListView.as_view(), name="listView"),
    path("", EstadoEntregaListView.as_view(), name="listView"),
]

app_name = 'EstadosEntrega'

urlpatterns = [
    re_path(r"^getEstadoEntrega$", EstadoEntregaListApi.as_view(), name="getEstadoEntrega"),
]