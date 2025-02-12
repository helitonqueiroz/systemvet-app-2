from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include(('clientes.urls', 'clientes'), namespace='clientes')),  # Inclui o namespace 'clientes'
    path('', include('core.urls')),  # Inclui as URLs do dashboard
]