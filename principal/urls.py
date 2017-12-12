from django.conf.urls import url
from views import *
from viewsHorarios import *
from viewsClientes import *
from viewTrabajadores import *

urlpatterns = [
url(r'insertarTrabajador/$',insertarTrabajador), 
url(r'guardarClientes/$',insertarClientes),
url(r'insertarHorario/$',insertarHorario),
url(r'^$',menu)

]
