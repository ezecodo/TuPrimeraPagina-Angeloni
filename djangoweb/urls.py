from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar 'include'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("web.urls")),  # Incluye las rutas de la app 'web'
]
