from django.urls import path
from django.urls import re_path
from EstadosPedidos.views import EstadoPedidoListView
from .views import EstadoPedidoListApi



urlpatterns = [
    path("EstadoPedidoListView/", EstadoPedidoListView.as_view(), name="listView"),
    path("", EstadoPedidoListView.as_view(), name="listView"),
]

app_name = 'EstadosPedido'

urlpatterns = [
    re_path(r"^getEstadoPedido$", EstadoPedidoListApi.as_view(), name="getEstadoPedido"),
]