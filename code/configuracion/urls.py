from django.urls import path
from . import views

urlpatterns= [ 
        path('', views.index,name='index'),
        path('<int:persona_id>/', views.consultaPersona, name='consultaPersona'),
        path('registrarHortelano/', views.registrarHortelano),
        path('editarHortelano/<int:id>/', views.editarHortelano),
       path('modificarHortelano/', views.modificarHortelano),
       path('eliminarHortelano/<int:id>/', views.eliminarHortelano),
       
]