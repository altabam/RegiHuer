from django.urls import path
from . import views

app_name = 'accesibilidad'
urlpatterns= [ 
        path('cargaInicialMenu', views.cargaInicialMenu,name='cargaInicialMenu'),
        
]