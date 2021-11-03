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

    # USUARIOS

    path('usuarios', views.listado_usuarios, name='usuarios'),
    path('formulario_usuarios/<int:id>', views.formulario_usuarios, name='formulario_usuarios'),
    path('agregar_usuarios', views.agregar_usuarios, name='agregar_usuarios'),
    

]