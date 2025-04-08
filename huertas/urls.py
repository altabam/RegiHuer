from django.urls import path
from django.urls import include, re_path
from . import views
app_name = 'huertas'
urlpatterns= [ 

       path('gestion_huertas', views.gestion_huertas, name = 'gestion_huertas'),
       path('huertas/huerta_agregar/<int:id>/', views.huerta_agregar, name='huerta_agregar'),
       path('huertas/huerta_eliminar/<int:id>/', views.huerta_eliminar,name='huerta_eliminar'),
       path('huertas/huerta_editar/<int:id>/', views.huerta_editar,name='huerta_editar'),
       path('huerta_canteros_mostrar/<int:id>/', views.huerta_canteros_mostrar,name='huerta_canteros_mostrar'),
       
       path('huerta_cultivos_mostrar/<int:id>/', views.huerta_cultivos_mostrar,name='huerta_cultivos_mostrar'),
       path('huertas/huerta_cultivos_agregar/<int:id>/', views.huerta_cultivos_agregar, name='huerta_cultivos_agregar'),
       
       path('cantero_agregar/<int:id>/', views.cantero_agregar, name='cantero_agregar'),
       path('cantero_eliminar/<int:id>/', views.cantero_eliminar),
       path('cantero_editar/<int:id>/', views.cantero_editar),
       path('cantero_mostrar/<int:id>/', views.cantero_mostrar, name='cantero_mostrar'),
       
       path('canteros_listar/', views.canteros_listar, name='canteros_listar'),
       

       path('cantero_cultivos_agregar/<int:id>/', views.cantero_cultivos_agregar, name='cantero_cultivos_agregar'),
       path('cantero_cultivos_eliminar/<int:id>/', views.cantero_cultivos_eliminar),
       path('cantero_cultivos_editar/<int:id>', views.cantero_cultivos_editar),
       path('cantero_cultivos_mostrar/<int:id>/', views.cantero_cultivos_mostrar, name='cantero_cultivos_mostrar'),








]