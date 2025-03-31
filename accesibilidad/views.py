from django.shortcuts import render
from django.contrib.auth.models import Group
from .models import MenuGroup
# Create your views here.
def ObtenerMenu(user):
    print(user)
    group =Group.objects.filter(user=user)
    menuUsuario = MenuGroup.objects.filter(groups__in = group, menu__nivel=1)
    #menu = Menu.objects.filter(id__in = menuUsuario.menu_id)
    print(menuUsuario )
    #permisos = MenuGroup.objects.filter(groups= user.groups)
  #  print(permisos)
   # return Menu.objects.all()
    return menuUsuario
