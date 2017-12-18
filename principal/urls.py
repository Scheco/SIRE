from django.conf.urls import url
from views import *
from viewsHorarios import *
from viewsClientes import *
from viewTrabajadores import *
from viewsProveedores import *
from viewsNegocios import *
from viewsCamiones import *

urlpatterns = [
# ----------------URLS proveedores------------------
url(r'guardarProveedores/$',insertarProveedores),
url(r'proveedores/$',insertarProveedores),


# --------------URLS camiones----------------------
url(r'eliminarCamiones/$',eliminarCamion),
url(r'modificarCamiones/$',modificarCamion),
url(r'consultarCamion/$',consultarCamion),
url(r'InsertarCamiones/$',insertarCamion),
# url(r'guardarCamion/$',insertarCamion),


# -------------URLS proveedores-----------------
# url(r'consltarTrabajadores/$',consltarTrabajadores),      (hay problemas con esta url)
url(r'trabajadores/$',trabajadores),
url(r'insertarTrabajador/$',insertarTrabajador),


# -----------URLS horarios------------------
url(r'insertarHorario/$',insertarHorario),
url(r'consultarHorarios/$',consultarHorarios),
url(r'modificarHorarios/$',modificarHorarios),
url(r'guardarHorarios/$',guardarHorarios),
url(r'horariosEliminar/$',horariosEliminar),
url(r'eliminarHorarios/$',eliminarHorarios),

# -------------URLS clientes--------------------
url(r'eliminarCli/$',eliminarCli),
url(r'eliminarCliente/$',eliminarCliente),
url(r'guardarCambiosClientes/$',guardarCambiosClientes),
url(r'modificarClientes/$',modificarClientes),
url(r'consultarClientes/$',consultarClientes),
url(r'guardarClientes/$',insertarClientes),
url(r'clientes/$',insertarClientes),

# ---------------URLS negocios----------------------
url(r'eliminarNegocios/$',eliminarNegocios),
url(r'eliminarNeg/$',eliminarNeg),
url(r'guardarNegocios/$',guardarNegocios),
url(r'consultarNegocios/modificarNegocio/$',modificarNegocios),
url(r'consultarNegocios/$',consultarNegocios),
url(r'insertarNegocios/$',insertarNegocios),
url(r'negocios/$',insertarNegocios),





url(r'^$',menu),

]
