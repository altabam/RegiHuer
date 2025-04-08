from django.urls import path
from . import views

app_name = 'accesibilidad'
urlpatterns= [ 
        path('menu_carga_inicial', views.menu_carga_inicial,name='menu_carga_inicial'),
        path('gestion_menu', views.gestion_menu,name='gestion_menu'),
        path('menu_eliminar', views.menu_eliminar,name='menu_eliminar'),
        
]