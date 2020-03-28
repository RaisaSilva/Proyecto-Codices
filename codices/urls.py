from django.urls import path
from django.conf.urls import url 
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('deportes/', views.deportes, name='deportes'),
    path('arte/', views.arte, name='arte'),
    path('educacion/', views.educacion, name='educacion'),
    path('tecnologia/', views.tecnologia, name='tecnologia'),
    path('registro_docente/', views.registro_docente, name='registro_docente'),
    path('registro_estudiante/', views.registro_estudiante, name='registro_estudiante'),
    #path('', views.inicio_sesion_estudiante, name='inicio_sesion_estudiante'),
    path('inicio_sesion_docente/', views.inicio_sesion_docente, name='inicio_sesion_docente'),
    #url(r'^$', views.home),
    #url(r'^inicio_sesion_estudiante/$', login, {'template_name':'IniciarSesion/Estudiante/iniciaSesionEstudiante.html'}),
    path('inicio_sesion_estudiante/', LoginView.as_view(template_name='IniciarSesion/Estudiante/iniciaSesionEstudiante.html'), name="inicio_sesion_estudiante"),
    path('logout/', LogoutView.as_view(template_name='Inicio/inicio.html'), name="inicio"),
   # url(r'^logout/$',LogoutView, {'template_name': 'Inicio/inicio.html'} )
]

