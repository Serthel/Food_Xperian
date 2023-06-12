from django.urls import path
from django.urls import re_path
from DatosDomicilio.views import DatoDomicilioListView
from .views import DatoDomicilioListApi


urlpatterns = [
    path("DatoDomiciliolistView/", DatoDomicilioListView.as_view(), name="listView"),
    path("", DatoDomicilioListView.as_view(), name="listView"),
]

app_name = 'DatosDomicilio'

urlpatterns = [
    re_path(r"^getDatoDomicilio$", DatoDomicilioListApi.as_view(), name="getDatoDomicilio"),
]