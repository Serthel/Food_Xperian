from django.urls import path
from django.urls import re_path
from RegistrosMensajes.views import RegistroMensajeListView
from .views import RegistroMensajeListApi, RegistroMensajeSerializer


urlpatterns = [
    path("RegistroMensajeListView/", RegistroMensajeListView.as_view(), name="listView"),
    path("", RegistroMensajeListView.as_view(), name="listView"),
]

app_name = 'RegistrosMensaje'

urlpatterns = [
    re_path(r"^getRegistroMensaje$", RegistroMensajeListApi.as_view(), name="getRegistroMensaje"),
    re_path(r"^createRegistroMensaje", RegistroMensajeSerializer.as_view(), name="createRegistroMensaje"),
]