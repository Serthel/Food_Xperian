from django.urls import path
from django.urls import re_path
from TiposMetodosPago.views import TipoMetodoPagoListView
from .views import TipoMetodoPagoListApi


urlpatterns = [
    path("TipoMetodoPagoListView/", TipoMetodoPagoListView.as_view(), name="listView"),
    path("", TipoMetodoPagoListView.as_view(), name="listView"),
]

app_name = 'TiposMetodosPagos'

urlpatterns = [
    re_path(r"^getTipoMetodoPago$", TipoMetodoPagoListApi.as_view(), name="getTipoMetodoPago"),
]