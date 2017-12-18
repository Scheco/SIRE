from django.conf.urls import url
from views import *
from viewsHorarios import *
from viewsClientes import *
from viewTrabajadores import *
from viewsProveedores import *

urlpatterns = [
url(r'consltarTrabajadores/$',consltarTrabajadores),
url(r'trabajadores/$',trabajadores),
url(r'guardarProveedores/$',insertarProveedores),
url(r'proveedores/$',insertarProveedores),
url(r'insertarTrabajador/$',insertarTrabajador),

url(r'eliminarCli/$',eliminarCli),
url(r'eliminarCliente/$',eliminarCliente),
url(r'guardarCambiosClientes/$',guardarCambiosClientes),
url(r'modificarClientes/$',modificarClientes),

url(r'consultarClientes/$',consultarClientes),
url(r'guardarClientes/$',insertarClientes),
url(r'clientes/$',insertarClientes),


url(r'insertarHorario/$',insertarHorario),
url(r'^$',menu)

]
