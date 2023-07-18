from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mantenciones/', views.mantenciones, name='mantenciones'),
    path('mantenciones/nueva/', views.nueva_mantencion, name='nueva_mantencion'),
    path('mantenciones/editar/<int:id>/', views.editar_mantencion, name='editar_mantencion'),
    path('mantenciones/eliminar/<int:id>/', views.eliminar_mantencion, name='eliminar_mantencion'),
    path('vehiculos/', views.listado_vehiculos, name='vehiculos'),
    path('vehiculos/nuevo/', views.nuevo_vehiculo, name='nuevo_vehiculo'),
    path('vehiculos/editar/<int:id>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('vehiculos/eliminar/<int:id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('personal/nuevo/', views.nuevo_personal, name='nuevo_personal'),
    path('personal/editar/<int:id>/', views.editar_personal, name='editar_personal'),
    path('personal/eliminar/<int:id>/', views.eliminar_personal, name='eliminar_personal'),
    path('personal/', views.lista_personal, name='personal'),
]