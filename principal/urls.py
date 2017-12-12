from django.conf.urls import url
from views import *
from viewsClientes import *

urlpatterns = [
url(r'guardarClientes/$',insertarClientes),
url(r'^$',menu)

]
