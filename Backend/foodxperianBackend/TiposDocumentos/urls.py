from django.urls import path
from django.urls import re_path
from TiposDocumentos.views import TipoDocumentoListView
from .views import TipoDocumentoListApi

urlpatterns = [
    path("TipoDocumentoListView/", TipoDocumentoListView.as_view(), name="listView"),
    path("", TipoDocumentoListView.as_view(), name="listView"),
]

app_name = 'TiposDocumento'

urlpatterns2 = [
    re_path(r"^getTipoDocumento$", TipoDocumentoListApi.as_view(), name="getTipoDocumento"),
]