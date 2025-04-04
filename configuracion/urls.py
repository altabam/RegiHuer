from django.urls import path
from django.urls import include, re_path
from . import views
app_name = 'configuracion'
urlpatterns= [ 
       path('gestion_hortelanos', views.gestion_hortelanos,name='gestion_hortelanos'),
       path('configuracion/consultaPersona/<int:persona_id>/', views.consultaPersona, name='consultaPersona'),
       path('configuracion/registrarHortelano/', views.registrarHortelano),
       path('hortelano_editar/<int:id>/', views.hortelano_editar, name='hortelano_editar'),
       path('hortelano_modificar/', views.hortelano_modificar),
       path('hortelano_eliminar/<int:id>', views.hortelano_eliminar),

       path('gestion_huertas', views.gestion_huertas, name = 'gestion_huertas'),
       path('configuracion/huerta_agregar/<int:id>/', views.huerta_agregar, name='huerta_agregar'),
       path('configuracion/huerta_eliminar/<int:id>/', views.huerta_eliminar,name='huerta_eliminar'),
       path('configuracion/huerta_editar/<int:id>/', views.huerta_editar,name='huerta_editar'),
       path('configuracion/huerta_canteros_mostrar/<int:id>/', views.huerta_canteros_mostrar,name='huerta_canteros_mostrar'),
       
       path('configuracion/huerta_cultivos_mostrar/<int:id>/', views.huerta_cultivos_mostrar,name='huerta_cultivos_mostrar'),
       path('configuracion/huerta_cultivos_agregar/<int:id>/', views.huerta_cultivos_agregar, name='huerta_cultivos_agregar'),
       
       path('configuracion/cantero_agregar/<int:id>/', views.cantero_agregar, name='cantero_agregar'),
       path('configuracion/cantero_eliminar/<int:id>/', views.cantero_eliminar),
       path('configuracion/cantero_editar/<int:id>/', views.cantero_editar),
       path('configuracion/cantero_mostrar/<int:id>/', views.cantero_mostrar, name='cantero_mostrar'),
       
       path('configuracion/canteros_listar/', views.canteros_listar, name='canteros_listar'),
       

       path('configuracion/cantero_cultivos_agregar/<int:id>/', views.cantero_cultivos_agregar, name='cantero_cultivos_agregar'),
       path('configuracion/cantero_cultivos_eliminar/<int:id>/', views.cantero_cultivos_eliminar),
       path('configuracion/cantero_cultivos_editar/<int:id>', views.cantero_cultivos_editar),
       path('configuracion/cantero_cultivos_mostrar/<int:id>/', views.cantero_cultivos_mostrar, name='cantero_cultivos_mostrar'),

       path('gestion_cultivos', views.gestion_cultivos, name = 'gestion_cultivos'),
       path('cultivo_agregar', views.cultivo_agregar, name='cultivo_agregar'),
       path('cultivo_eliminar/<int:id>', views.cultivo_eliminar, name='cultivo_eliminar'),
       path('cultivo_editar/<int:id>', views.cultivo_editar, name='cultivo_editar'),
       re_path(r'^configuracion/cultivo_buscar', views.cultivo_buscar, name ='cultivo_buscar'),


       path('tierras_cultivo_listar/', views.tierras_cultivo_listar, name = 'tierras_cultivos_listar'),
       path('configuracion/tierras_cultivo_agregar/', views.tierras_cultivo_agregar, name='tierras_cultivo_agregar'),
       path('configuracion/tierras_cultivo_eliminar/<int:id>/', views.tierras_cultivo_eliminar, name='tierras_cultivo_eliminar'),
       path('configuracion/tierras_cultivo_editar/<int:id>/', views.tierras_cultivo_editar, name='tierras_cultivo_editar'),

       path('enfermedades_listar/', views.enfermedades_listar, name = 'enfermedades_listar'),
       path('configuracion/enfermedades_agregar/', views.enfermedades_agregar, name='enfermedades_agregar'),
       path('configuracion/enfermedades_eliminar/<int:id>/', views.enfermedades_eliminar, name='enfermedades_eliminar'),
       path('configuracion/enfermedades_editar/<int:id>/', views.enfermedades_editar, name='enfermedades_editar'),

       path('plagas_listar/', views.plagas_listar, name = 'plagas_listar'),
       path('configuracion/plagas_agregar/', views.plagas_agregar, name='plagas_agregar'),
       path('configuracion/plagas_eliminar/<int:id>/', views.plagas_eliminar, name='plagas_eliminar'),
       path('configuracion/plagas_editar/<int:id>/', views.plagas_editar, name='plagas_editar'),


       path('gestion_img_galeria_principal', views.gestion_img_galeria_principal, name='gestion_img_galeria_principal'),
       path('configuracion/galeria_imagenes_agregar/', views.galeria_imagenes_agregar, name='galeria_imagenes_agregar'),
       path('configuracion/galeria_imagenes_eliminar/<int:id>/', views.galeria_imagenes_eliminar, name='galeria_imagenes_eliminar'),
       path('configuracion/galeria_imagenes_editar/<int:id>/', views.galeria_imagenes_editar, name='galeria_imagenes_editar'),



]