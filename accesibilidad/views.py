from django.shortcuts import render
from django.contrib.auth.models import Group
from .models import MenuGroup, Menu
import csv
# Create your views here.
def gestion_menu(request):
    menu = Menu.objects.all()
    contexto ={"listadoMenu":menu,
               "menu": generarMenu("hola")
    }

    return render(request, "gestion_menu.html",contexto)

def menu_eliminar(request):
    Menu.objects.all().delete()
    menu = Menu.objects.all()
    contexto ={"menu":menu,
    }

    return render(request, "gestion_menu.html",contexto)


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


def generarTagPrincipalHoja(menu, orden):
    if orden > 1:
      menuTitle = 'menu-title_'+str(orden)
    else:
        menuTitle=''
    me =[]
    tag = [{'tag':'<li>'}]
    me = [tag]
    
    tag = []
    tag.append({'tag':'<a>','href':menu.url, 'class':'menu'})
    me.append(tag)
    
    tag =[]
    tag.append({'tag':'<h2>', 'class':'menu-title '+menuTitle, 'descripcion':menu.nombre})
    me.append(tag)
    
    tag =[]
    tag.append({'tag':'<ul>', 'class':'menu-dropdown', })
    me.append(tag)

    tag =[]
    tag.append({'tag':'</ul>'})
    me.append(tag)
    
    tag =[]
    tag.append({'tag':'</a>'})
    me.append(tag)
    
    tag =[]
    tag.append({'tag':'</li>'})
    me.append(tag)
  
    return me
def generarTagPrincipalPadre(menu,orden):
    if orden > 1:
      menuTitle = 'menu-title_'+str(orden)
    else:
        menuTitle=''
    me =[]
    tag = [{'tag':'<li>'}]
    me = [tag]
    
    tag = []
    tag.append({'tag':'<div>','class':'menu'})
    me.append(tag)
    tag =[]

    tag.append({'tag':'<h2>', 'class':'menu-title '+menuTitle, 'descripcion':menu.nombre})
    me.append(tag)
    tag =[]
    tag.append({'tag':'<ul>', 'class':'menu-dropdown', })
    me.append(tag)
    menuHijos = Menu.objects.filter(menuPadre = menu)
    #print("menu hijo:", menuHijos)
    for mh in menuHijos:
        tag=[]
        if mh.tipo=='H':
            print('tag hijo mh:', mh)
            tag.append({'tag':'<li>'})
            me.append(tag)
 
            tag=[]
            tag.append({'tag':'<a>','href':mh.url, 'class':'menu', 'descripcion':mh.nombre})
            me.append(tag)
        
            tag =[]
            tag.append({'tag':'</a>'})
            me.append(tag)

            tag=[]
            tag.append({'tag':'</li>'})
            me.append(tag)
    tag =[]
    tag.append({'tag':'</ul>'})
    me.append(tag)
    tag =[]
    tag.append({'tag':'</div>'})
    me.append(tag)
    tag =[]
    tag.append({'tag':'</li>'})
    me.append(tag)
  


    return me
def generarMenu(user):
  menu =[]
  menues = Menu.objects.filter( menuPadre__isnull = True )
  orden = 1
  for me in menues:
      if me.tipo=="H":
          menu.extend(generarTagPrincipalHoja(me,orden))
      elif me.tipo == 'P':
          menu.extend(generarTagPrincipalPadre(me,orden))
      if orden == 4:
       orden =1
      else:
        orden +=1
   
  #print(menues)
  #print("menu generado:",menu)
  return menu


def menu_carga_inicial(request):
    template_name = "accesibilidad/migrations/menues.csv"
    model = Menu()
    #Disciplinas.objects.all().delete()
    with open (template_name) as f:
        reader = csv.reader(f )
        for row in reader:
         #  print("row:",row)
           if  not Menu.objects.filter(nombre = row[1]).exists():
               if  Menu.objects.filter(nombre = row[3]).exists():
                 #  print("dentro de Menu Padre:", row[3])
                   menuP = Menu.objects.get(nombre = row[3])
                   model.menuPadre = menuP
                   Menu.objects.create(url = row[0], nombre =row[1] ,tipo = row[2],menuPadre = menuP)
               else:
                   print("No hay de Menu Padre:", row[3])
                   Menu.objects.create(url = row[0], nombre =row[1], tipo = row[2])
    mensaje ="carga con exito"
    contexto ={  
        "mensaje":mensaje , 
        "menu": generarMenu(request.user),
        "listadoMenu": Menu.objects.all(), 
    } 
    return render (request, "gestion_menu.html",contexto)
