from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('acceder', views.acceder, name='acceder'),

    # Empresa 
    path('lista_empresa', views.listado_empresa, name='lista_empresa'),
    path('formulario_empresa/<int:id>', views.formulario_empresa, name='formulario_empresa'),
    path('agregar_empresa', views.agregar_empresa, name='agregar_empresa'),
    
    # Encargado
    
    path('encargado', views.listado_encargado, name='encargado'),
    path('formulario_encargado/<int:id>', views.formulario_encargado, name='formulario_encargado'),
    path('agregar_encargado', views.agregar_encargado, name='agregar_encargado'), 
      
    # DOCUMENTACION
    path('compromisos', views.formulario_compromisos, name='configuracion_empresa'),
    path('riesgos', views.formulario_riesgos, name='riesgos'),
    path('plan_emergencia', views.formulario_plan_emergencia, name='plan_emergencia'),

    # ALIADOS

    path('aliados', views.listado_aliados, name='aliados'),
    path('formulario_aliados/<int:id>', views.formulario_aliados, name='formulario_aliados'),
    path('agregar_aliados', views.agregar_aliados, name='agregar_aliados'),
    path('eliminar_aliados/<int:id>', views.eliminar_aliados, name='eliminar_aliados'),
    
    path('formulario_productos/<int:id>/<int:aliado>', views.formulario_productos ,name='formulario_productos'),
    path('agregar_productos', views.agregar_productos, name='agregar_productos'),

    # USUARIOS

    path('usuarios', views.listado_usuarios, name='usuarios'),
    path('formulario_usuarios/<int:id>', views.formulario_usuarios, name='formulario_usuarios'),
    path('agregar_usuarios', views.agregar_usuarios, name='agregar_usuarios'),
    path('eliminar_usuarios/<int:id>', views.eliminar_usuarios, name='eliminar_usuarios'),

    #POLITICAS

    path('formulario_politicas/<int:id>', views.formulario_politicas, name='formulario_politicas'),
    path('agregar_politicas', views.agregar_politicas, name='agregar_politicas'),
    path('politicas', views.ver_politicas, name='politicas'),
    path('eliminar_politicas/<int:id>', views.eliminar_politicas, name='eliminar_politicas'),
    path('pdf_politicas/<int:id>', views.pdf_politicas, name='pdf_politicas'),
]