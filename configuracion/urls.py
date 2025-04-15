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

       path('gestion_cultivos', views.gestion_cultivos, name = 'gestion_cultivos'),
       path('cultivo_agregar', views.cultivo_agregar, name='cultivo_agregar'),
       path('cultivo_eliminar/<int:id>', views.cultivo_eliminar, name='cultivo_eliminar'),
       path('cultivo_editar/<int:id>', views.cultivo_editar, name='cultivo_editar'),
       re_path(r'^configuracion/cultivo_buscar', views.cultivo_buscar, name ='cultivo_buscar'),


       path('gestion_tierras_cultivo/', views.gestion_tierras_cultivo, name = 'gestion_tierras_cultivo'),
       path('configuracion/tierras_cultivo_agregar/', views.tierras_cultivo_agregar, name='tierras_cultivo_agregar'),
       path('configuracion/tierras_cultivo_eliminar/<int:id>/', views.tierras_cultivo_eliminar, name='tierras_cultivo_eliminar'),
       path('configuracion/tierras_cultivo_editar/<int:id>/', views.tierras_cultivo_editar, name='tierras_cultivo_editar'),

       path('gestion_temperaturas/', views.gestion_temperaturas, name = 'gestion_temperaturas'),
       path('configuracion/temperaturas_agregar/', views.temperaturas_agregar, name='temperaturas_agregar'),
       path('configuracion/temperaturas_eliminar/<int:id>/', views.temperaturas_eliminar, name='temperaturas_eliminar'),
       path('configuracion/temperaturas_editar/<int:id>/', views.temperaturas_editar, name='temperaturas_editar'),

       path('gestion_luz_cultivos/', views.gestion_luz_cultivos, name = 'gestion_luz_cultivos'),
       path('configuracion/luz_cultivos_agregar/', views.luz_cultivos_agregar, name='luz_cultivos_agregar'),
       path('configuracion/luz_cultivos_eliminar/<int:id>/', views.luz_cultivos_eliminar, name='luz_cultivos_eliminar'),
       path('configuracion/luz_cultivos_editar/<int:id>/', views.luz_cultivos_editar, name='luz_cultivos_editar'),

       path('gestion_riego_cultivos/', views.gestion_riego_cultivos, name = 'gestion_riego_cultivos'),
       path('configuracion/riego_cultivos_agregar/', views.riego_cultivos_agregar, name='riego_cultivos_agregar'),
       path('configuracion/riego_cultivos_eliminar/<int:id>/', views.riego_cultivos_eliminar, name='riego_cultivos_eliminar'),
       path('configuracion/riego_cultivos_editar/<int:id>/', views.riego_cultivos_editar, name='riego_cultivos_editar'),

       path('gestion_enfermedades/', views.gestion_enfermedades, name = 'gestion_enfermedades'),
       path('configuracion/enfermedades_agregar/', views.enfermedades_agregar, name='enfermedades_agregar'),
       path('configuracion/enfermedades_eliminar/<int:id>/', views.enfermedades_eliminar, name='enfermedades_eliminar'),
       path('configuracion/enfermedades_editar/<int:id>/', views.enfermedades_editar, name='enfermedades_editar'),

       path('gestion_plagas/', views.gestion_plagas, name = 'gestion_plagas'),
       path('configuracion/plagas_agregar/', views.plagas_agregar, name='plagas_agregar'),
       path('configuracion/plagas_eliminar/<int:id>/', views.plagas_eliminar, name='plagas_eliminar'),
       path('configuracion/plagas_editar/<int:id>/', views.plagas_editar, name='plagas_editar'),

       path('configuracion_carga_inicial', views.configuracion_carga_inicial,name='configuracion_carga_inicial'),
       path('carga_inicial_tierra_cultivo', views.carga_inicial_tierra_cultivo,name='carga_inicial_tierra_cultivo'),
       path('eliminar_todo_tierra_cultivo', views.eliminar_todo_tierra_cultivo,name='eliminar_todo_tierra_cultivo'),

       path('gestion_img_galeria_principal', views.gestion_img_galeria_principal, name='gestion_img_galeria_principal'),
       path('configuracion/galeria_imagenes_agregar/', views.galeria_imagenes_agregar, name='galeria_imagenes_agregar'),
       path('configuracion/galeria_imagenes_eliminar/<int:id>/', views.galeria_imagenes_eliminar, name='galeria_imagenes_eliminar'),
       path('configuracion/galeria_imagenes_editar/<int:id>/', views.galeria_imagenes_editar, name='galeria_imagenes_editar'),



]