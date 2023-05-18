# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
app_name = "home" 
urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    
    path('cliente/',views.cliente_lista, name='cliente_lista'),
    path('cliente-registro/',views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cliente/delete/<int:id>', views.deletar_cliente),
    path('cliente/editar/<int:id>', views.atualizar_cliente, name="atualizar_cliente"), 

]
