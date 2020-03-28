"""djangolab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls import url
from codices import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('codices/', include('codices.urls')),
    path('admin/', admin.site.urls),
    #url(r'^deportes/', views.deportes, name='deportes'),
    #url(r'^arte/', views.arte, name='arte'),
    #url(r'^tecnologia/', views.tecnologia, name='tecnologia'),
    #url(r'^educacion/', views.educacion, name='educacion'),
    #url(r'^registro_docente/', views.registro_docente, name='registro_docente'),
    #url(r'^registro_estudiante/', views.registro_estudiante, name='registro_estudiante'),
    #url(r'^inicio_sesion_estudiante/', views.inicio_sesion_estudiante, name='inicio_sesion_estudiante'),
    #url(r'^inicio_sesion_docente/', views.inicio_sesion_docente, name='inicio_sesion_docente'),
    re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,}),
]
