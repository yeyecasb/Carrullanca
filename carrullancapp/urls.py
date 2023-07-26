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
    path('proyectos/nuevo/', views.crear_proyecto, name='nuevo_proyecto'),
    path('proyectos/editar/<int:id>/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/eliminar/<int:id>/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('proyectos/', views.lista_proyectos, name='proyectos'),
    path('analisis/new_material_cost/<int:id>/', views.material_cost_new, name='material_cost_new'),
    path('analisis/new_labor_cost/<int:pk>/', views.labor_cost_new, name='labor_cost_new'),
    path('analisis/new_equipment_cost/<int:pk>/', views.equipament_cost_new, name='equipment_cost_new'),
    path('analisis/historial/<int:pk>/', views.analisis_historial, name='analisis_historial'),
    path('analisis/', views.analisis_list, name='analisis_list'),
    path('analisis/new/', views.analisis_new, name='analisis_new'),
]