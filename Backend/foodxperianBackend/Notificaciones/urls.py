from django.urls import path
from django.urls import re_path
from Notificaciones.views import NotificacionListView
from .views import NotificacionListApi



urlpatterns = [
    path("NotificacionListView/", NotificacionListView.as_view(), name="listView"),
    path("", NotificacionListView.as_view(), name="listView"),
]

app_name = 'Notificaciones'

urlpatterns = [
    re_path(r"^getNotificacion$", NotificacionListApi.as_view(), name="getNotificacion"),
]