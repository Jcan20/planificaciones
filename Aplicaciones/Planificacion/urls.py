from django.urls import path
from . import views
urlpatterns =[
     path('', views.inicio, name='inicio'),  # Esta ruta carga la vista 'inicio'
     path('constructoras/', views.listadoConstructoras, name='listadoConstructoras'),
     path('constructoras/nueva/', views.nuevaConstructora, name='nuevaConstructora'),
     path('constructoras/guardar/', views.guardarConstructora, name='guardarConstructora'),
     path('constructoras/editar/<int:id>/', views.editarConstructora, name='editarConstructora'),
     path('constructoras/actualizar/', views.actualizarConstructora, name='actualizarConstructora'),
     path('constructoras/eliminar/<int:id>/', views.eliminarConstructora, name='eliminarConstructora'),
     #CLIENTES
     path('listado/', views.listadoClientes, name='listadoClientes'),  # Listado de Clientes
    path('nuevo/', views.nuevoCliente, name='nuevoCliente'),  # Formulario de Nuevo Cliente
    path('guardar/', views.guardarCliente, name='guardarCliente'),  # Guardar Cliente
    path('editar/<int:id>/', views.editarCliente, name='editarCliente'),  # Editar Cliente
    path('actualizar/<int:id>/', views.actualizarCliente, name='actualizarCliente'),
    path('eliminar/<int:id>/', views.eliminarCliente, name='eliminarCliente'),  # Eliminar Cliente
    #VIVIENDA
    path('viviendas/', views.listadoViviendas, name='listadoViviendas'),
    path('vivienda/nueva/', views.nuevaVivienda, name='nuevaVivienda'),
    path('vivienda/guardar/', views.guardarVivienda, name='guardarVivienda'),
    path('vivienda/editar/<int:id>/', views.editarVivienda, name='editarVivienda'),
    path('vivienda/actualizar/<int:id>/', views.actualizarVivienda, name='actualizarVivienda'),
    path('vivienda/eliminar/<int:id>/', views.eliminarVivienda, name='eliminarVivienda'),
    #ACTIVIDAD
     path('actividades/', views.listadoActividades, name='listadoActividades'),
    path('actividades/nueva/', views.nuevaActividad, name='nuevaActividad'),
    path('actividades/guardar/', views.guardarActividad, name='guardarActividad'),
    path('actividades/editar/<int:id>/', views.editarActividad, name='editarActividad'),
    path('actividades/actualizar/<int:id>/', views.actualizarActividad, name='actualizarActividad'),
    path('actividades/eliminar/<int:id>/', views.eliminarActividad, name='eliminarActividad'),
    path('actividades/enviar-correo/<int:id>/', views.enviar_correo_actividad, name='enviarCorreoActividad'),
    
    ]