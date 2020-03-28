from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


# Create your views here.
def inicio(request):
	return render_to_response("Inicio/inicio.html")

def deportes(request):
	deportes_list = Curso.objects.all().filter(categoria = "Deportes")
	context = {'curso_deportes' : deportes_list}
	return render_to_response("Deportes/deportes.html", context)
	
def arte(request):
	arte_list = Curso.objects.all().filter(categoria = "Arte")
	context = {'curso_arte': arte_list}
	return render_to_response("Arte/arte.html", context)

def educacion(request):
	educacion_list = Curso.objects.all().filter(categoria = "Educación")
	context = {'curso_educacion': educacion_list}
	return render_to_response("Educacion/educacion.html")

def tecnologia(request):
	tecnologia_list = Curso.objects.all().filter(categoria = "Tecnología")
	context = {'curso_tecnologia': tecnologia_list}
	return render_to_response("Tecnologia/tecnologia.html", context)

def registro_docente(request):
	return render_to_response("Registros/RegistroDocente/registro_docente.html")

def registro_estudiante(request):
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/codices/inicio')
	else:
		form = UserCreationForm()
		args = {'form': form}
		return render(request,  'Registros/RegistroEstudiante/registro_estudiante.html', args)#
	return render_to_response("Registros/RegistroEstudiante/registro_estudiante.html")#


def inicio_sesion_estudiante(request):
	return render_to_response("IniciarSesion/Estudiante/iniciaSesionEstudiante.html")

def inicio_sesion_docente(request):
	return render_to_response("IniciarSesion/Docente/iniciaSesionDocente.html")