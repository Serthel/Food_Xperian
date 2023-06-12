from django.urls import path
from django.urls import re_path
from Pedidos.views import PedidoListView
from .views import PedidoListApi



urlpatterns = [
    path("PedidoListView/", PedidoListView.as_view(), name="listView"),
    path("", PedidoListView.as_view(), name="listView"),
]

app_name = 'Pedidos'

urlpatterns = [
    re_path(r"^getPedido$", PedidoListApi.as_view(), name="getPedido"),
]