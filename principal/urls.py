from django.conf.urls import url
from views import *
from viewsHorarios import *
from viewsClientes import *
from viewTrabajadores import *
from viewsProveedores import *
from viewsMateriales import *

urlpatterns = [
url(r'consltarTrabajadores/$',consltarTrabajadores),
url(r'trabajadores/$',trabajadores),
url(r'guardarProveedores/$',insertarProveedores),
url(r'proveedores/$',insertarProveedores),
url(r'insertarTrabajador/$',insertarTrabajador),
url(r'guardarClientes/$',insertarClientes),
url(r'insertarHorario/$',insertarHorario),
url(r'insertarMateriales/$',insertarMateriales),
url(r'consultarMateriales/$',consultarMateriales),
url(r'modificarM/$',modificarM),
url(r'modificarMateriales/$',modificarMateriales),
url(r'eliminarM/$',eliminarM),
url(r'eliminarMateriales/$',eliminarMateriales),
url(r'^$',menu)

]
