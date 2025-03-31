from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from . import views    
urlpatterns = [
    path('', views.index,name='index'),
    path('registracion', views.registrar,name='registrar'),
    path('validacion', views.mailValidador,name='mailValidador'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)