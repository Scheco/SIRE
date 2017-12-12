from django.conf.urls import url
from views import *
<<<<<<< HEAD
from viewsClientes import *

urlpatterns = [
url(r'guardarClientes/$',insertarClientes),
=======
from viewsHorarios import *

urlpatterns = [
url(r'insertarHorario/$',insertarHorario),
>>>>>>> 8693ca1c412637f3631a1a6b79895cf1caeaa0ca
url(r'^$',menu)

]
