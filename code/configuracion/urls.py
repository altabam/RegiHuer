from django.urls import path
from . import views

urlpatterns= [ 
       path('', views.index,name='index'),
       path('listadoHortelano/', views.listadoHortelano,name='listadoHortelano'),
       path('<int:persona_id>/', views.consultaPersona, name='consultaPersona'),
       path('configuracion/registrarHortelano/', views.registrarHortelano),
       path('configuracion/editarHortelano/<int:id>/', views.editarHortelano),
       path('configuracion/modificarHortelano/', views.modificarHortelano),
       path('configuracion/eliminarHortelano/<int:id>', views.eliminarHortelano),
       path('huertas_listar/', views.huertas_listar),
       path('configuracion/huerta_eliminar/<int:id>/', views.huerta_eliminar),
       path('configuracion/huerta_editar/<int:id>/', views.huerta_editar),
       path('configuracion/huerta_registrar/', views.huerta_registrar),
       path('configuracion/huerta_modificar/', views.huerta_modificar),
       path('configuracion/huerta_mostrar/<int:id>/', views.huerta_mostrar),
       path('configuracion/cantero_eliminar/<int:id>/', views.cantero_eliminar),
       path('configuracion/cantero_editar/<int:id>/', views.cantero_editar),
       path('configuracion/cantero_registrar/', views.cantero_registrar), 
       path('configuracion/cantero_modificar/', views.cantero_modificar),
       
]