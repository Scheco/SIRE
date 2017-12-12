from django.conf.urls import url
from views import *
from viewsHorarios import *

urlpatterns = [
url(r'insertarHorario/$',insertarHorario),
url(r'^$',menu)

]
