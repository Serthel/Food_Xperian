from django.urls import path
from django.urls import re_path
from TiemposEntrega.views import TiempoEntregaListView
from .views import TiempoEntregaListApi

urlpatterns = [
    path("TiempoEntregaListView/", TiempoEntregaListView.as_view(), name="listView"),
    path("", TiempoEntregaListView.as_view(), name="listView"),
]

app_name = 'TiemposEntrega'

urlpatterns = [
    re_path(r"^getTiempoEntrega$", TiempoEntregaListApi.as_view(), name="getTiempoEntrega"),
]