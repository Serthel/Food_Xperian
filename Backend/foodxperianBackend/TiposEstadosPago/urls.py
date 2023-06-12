from django.urls import path
from django.urls import re_path
from TiposEstadosPago.views import TiposEstadosPagoListView
from .views import TipoEstadoPagoListApi
urlpatterns = [
    path("TipoEstadoPagoListView/", TiposEstadosPagoListView.as_view(), name="listView"),
    path("", TiposEstadosPagoListView.as_view(), name="listView"),
]

app_name = 'TipoEstadosPago'

urlpatterns2 = [
    re_path(r"^getTipoEstadoPago$", TipoEstadoPagoListApi.as_view(), name="getTipoEstadoPago"),
]