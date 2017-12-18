from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from models import Horarios
from models import Negocios

def insertarHorario(request):

    # return render(request,"insertarHorario.html",{'msg':'Entra al metodo'});

    # if "id_horario" in request.POST and "id_negocio" in request.POST and "lunes" in request.POST and "hora_lunes" in request.POST and "martes" in request.POST and "hora_martes" in request.POST and "miercoles" in request.POST and "hora_miercoles" in request.POST and  "jueves" in request.POST and "hora_Jueves" in request.POST and "viernes" in request.POST and "hora_viernes" in request.POST and "sabado" in request.POST and "hora_sabado" in request.POST:
    if  "idHorario" in request.GET and "idNegocio" in request.GET and  "horaLunes" in request.GET and "horaMartes" in request.GET and "horaMiercoles" in request.GET and "horaJueves" in request.GET and "horaViernes" in request.GET and "horaSabado" in request.GET:
            # return render(request,"menu.html",{'msg':'Entra al if'});
            print "Procesando"
            negocios=Negocios.objects.all()
            return render(request,"insertarHorario.html",{'negocios':negocios})


            idHorario = request.GET['idHorario']
            idNegocio_id = request.GET['idNegocio']

            if "lunes" in request.GET:
                lunes = True
            else:
                lunes = False

            horaLunes = request.GET['horaLunes']

            if "martes" in request.GET:
                martes = True
            else:
                martes = False

            horaMartes = request.GET['horaMartes']

            if "miercoles" in request.GET:
                miercoles = True
            else:
                miercoles = False


            horaMiercoles = request.GET['horaMiercoles']

            if "jueves" in request.GET:
                jueves = True
            else:
                jueves = False


            horaJueves = request.GET['horaJueves']

            if "viernes" in request.GET:
                viernes = True
            else:
                viernes = False

            horaViernes = request.GET['horaViernes']

            if "sabado" in request.GET:
                sabado = True
            else:
                sabado = False

            horaSabado = request.GET['horaSabado']
            p = Horarios(idHorario=idHorario,idNegocio_id=idNegocio_id,lunes=lunes,horaLunes=horaLunes,martes=martes,horaMartes=horaMartes,miercoles=miercoles,horaMiercoles=horaMiercoles,jueves=jueves,horaJueves=horaJueves,viernes=viernes,horaViernes=horaViernes,sabado=sabado,horaSabado=horaSabado)
            p.save()
            # negocios=Negocios.objects.all()
            return render(request,"insertarHorario.html",{'msg': 'Se registro correctamente un nuevo horario'})
    else:
            return render(request,"insertarHorario.html")

def consultarHorarios(request):
    negocios=Negocios.objects.all()
    horarios=Horarios.objects.all()
    return render(request,'consultarHorarios.html',{'negocios':negocios,'horarios':horarios})

def consultarHorariosNegocios(request):
    negocios=Negocios.objects.all()
    return render(request,'insertarHorario.html',{'negocios':negocios})


def modificarHorarios(request):
    registro=Horarios.objects.get(idHorario=request.POST['idHorario'])
    return render(request,'modificarHorarios.html',{'reg':registro})

def guardarHorarios(request):
    reg=Horarios(idHorario = request.GET['idHorario'])
    reg.idNegocio_id = request.GET['idNegocio']

    if "lunes" in request.GET:
        lunes = True
    else:
        lunes = False

    horaLunes = request.GET['horaLunes']

    if "martes" in request.GET:
        martes = True
    else:
        martes = False

    horaMartes = request.GET['horaMartes']

    if "miercoles" in request.GET:
        miercoles = True
    else:
        miercoles = False


    horaMiercoles = request.GET['horaMiercoles']

    if "jueves" in request.GET:
        jueves = True
    else:
        jueves = False


    horaJueves = request.GET['horaJueves']

    if "viernes" in request.GET:
        viernes = True
    else:
        viernes = False

    horaViernes = request.GET['horaViernes']

    if "sabado" in request.GET:
        sabado = True
    else:
        sabado = False

    horaSabado = request.GET['horaSabado']

    reg.save()
    negocios=Negocios.objects.all()
    horarios=Horarios.objects.all()
    return render(request,'consultarHorarios.html')

def horariosEliminar(request):
    idHorario=request.POST['idHorario']
    horarios=Horarios.objects.filter(idHorario=idHorario)
    return render(request,'eliminarHorarios.html')

def eliminarHorarios(request):
    reg= Horarios(idHorario = request.POST['idHorario'])
    reg.delete()
    negocios= Negocios.objects.all()
    horarios=Horarios.objects.all()
    return render(request,'consultarHorarios.html')
