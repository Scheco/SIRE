from django.conf.urls import url
from views import *
from viewsHorarios import *
from viewsClientes import *
from viewTrabajadores import *
from viewsProveedores import *

urlpatterns = [
url(r'consultarHorarios/$',consultarHorarios),
url(r'consltarTrabajadores/$',consltarTrabajadores),
url(r'trabajadores/$',trabajadores),
url(r'guardarProveedores/$',insertarProveedores),
url(r'proveedores/$',insertarProveedores),
url(r'insertarTrabajador/$',insertarTrabajador),
url(r'guardarClientes/$',insertarClientes),
url(r'insertarHorario/$',insertarHorario),
url(r'^$',menu)

]
