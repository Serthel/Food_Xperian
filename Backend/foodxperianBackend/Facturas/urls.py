from django.urls import path
from django.urls import re_path
from Facturas.views import FacturaListView
from .views import FacturaListApi



urlpatterns = [
    path("FacturaListView/", FacturaListView.as_view(), name="listView"),
    path("", FacturaListView.as_view(), name="listView"),
]

app_name = 'Facturas'

urlpatterns = [
    re_path(r"^getFactura$", FacturaListApi.as_view(), name="getFactura"),

]