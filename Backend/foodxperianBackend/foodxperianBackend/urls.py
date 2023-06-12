"""
URL configuration for foodxperianBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from dj_rest_auth.registration.views import RegisterView


urlpatterns = [
path('admin/', admin.site.urls),
path('accounts/', include('allauth.urls')),
path("DatosDomicilio/", include("DatosDomicilio.urls")),
path("EstadosEntrega/", include("EstadosEntrega.urls")),
path("EstadosPedidos/", include("EstadosPedidos.urls")),
path("Facturas/", include("Facturas.urls")),
path("Notificaciones/", include("Notificaciones.urls")),
path("Pedidos/", include("Pedidos.urls")),
path("Producto/", include("Producto.urls")),
path("RegistrosMensajes/", include("RegistrosMensajes.urls")),
path("TiemposEntrega/", include("TiemposEntrega.urls")),
path("TiposDocumentos/", include("TiposDocumentos.urls")),
path("TiposEstadosPago/", include("TiposEstadosPago.urls")),
path("TiposMetodosPago/", include("TiposMetodosPago.urls")),
path('dj-rest-auth/', include('dj_rest_auth.urls')),
path('auth/registration/', RegisterView.as_view(), name='rest_register'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
