from django.conf.urls import url
from views import *
from viewsHorarios import *
from viewsClientes import *
from viewTrabajadores import *
from viewsProveedores import *
from viewsNegocios import *

urlpatterns = [
url(r'eliminarCamiones/$',eliminarCamion),
url(r'modificarCamiones/$',modificarCamion),
url(r'consultarCamion/$',consultarCamion),
url(r'insertarCamion/$',insertarCamion),
url(r'consltarTrabajadores/$',consltarTrabajadores),
url(r'trabajadores/$',trabajadores),
url(r'insertarNegocios/$',insertarNegocios),
url(r'guardarProveedores/$',insertarProveedores),
url(r'proveedores/$',insertarProveedores),
url(r'insertarTrabajador/$',insertarTrabajador),
url(r'guardarClientes/$',insertarClientes),
url(r'insertarHorario/$',insertarHorario),
url(r'consultarHorarios/$',consultarHorarios),
url(r'modificarHorarios/$',modificarHorarios),
url(r'guardarHorarios/$',guardarHorarios),
url(r'horariosEliminar/$',horariosEliminar),
url(r'eliminarHorarios/$',eliminarHorarios),
url(r'^$',menu)

]
