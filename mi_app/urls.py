from django.urls import path
from . import views

urlpatterns = [
    path('', views.mi_pagina_view, name='mi_pagina'),
]
