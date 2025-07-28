from django.urls import path
from . import views
from . views import inicio, ver_biografia, ver_proyectos, contacto, panel_admin, editar_biografia, listar_proyectos, crear_proyecto, editar_proyecto, eliminar_proyecto, listar_destacados, crear_destacado, editar_destacado, eliminar_destacado
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('biografia/', views.ver_biografia, name='biografia'),
    path('proyectos/', views.ver_proyectos, name='proyectos'),
    path('contacto/', views.contacto, name='contacto'),
     # Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='sitio/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    path('panel/', views.panel_admin, name='panel'),
    path('panel/editar-biografia/', views.editar_biografia, name='editar_biografia'),

    # CRUD Proyectos
    path('panel/proyectos/', views.listar_proyectos, name='listar_proyectos'),
    path('panel/proyectos/nuevo/', views.crear_proyecto, name='crear_proyecto'),
    path('panel/proyectos/editar/<int:proyecto_id>/', views.editar_proyecto, name='editar_proyecto'),
    path('panel/proyectos/eliminar/<int:proyecto_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),

    # CRUD Destacados
    path('panel/destacados/', views.listar_destacados, name='listar_destacados'),
    path('panel/destacados/nuevo/', views.crear_destacado, name='crear_destacado'),
    path('panel/destacados/editar/<int:destacado_id>/', views.editar_destacado, name='editar_destacado'),
    path('panel/destacados/eliminar/<int:destacado_id>/', views.eliminar_destacado, name='eliminar_destacado'),


]
