from django.urls import path
from django.urls import re_path
from Producto.views import ProductoListView
from .views import ProductoListApi,ProductoSerializer



urlpatterns = [
    path("ProductoListView/", ProductoListView.as_view(), name="listView"),
    path("", ProductoListView.as_view(), name="listView"),
]

app_name = 'Producto'

urlpatterns = [
    re_path(r"^getProducto$", ProductoListApi.as_view(), name="getProducto"),
    re_path(r"^createProducto", ProductoSerializer.as_view(), name="createProducto"),
]