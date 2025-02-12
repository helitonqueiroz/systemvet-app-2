# clientes\urls.py

from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registrar/', views.registrar_view, name='registrar'),
]
