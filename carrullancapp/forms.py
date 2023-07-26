from django import forms
from .models import Vehiculos, MantencionVehiculos, Personal, Proyectos, MaterialCost, LaborCost, EquipmentCost, AnalisisPreciosUnitarios

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculos
        fields = ['patente', 'marca', 'modelo', 'serie_motor', 'serie_chasis', 'anio', 'categoria', 'combustible', 'fecha_adquisicion', 'km_adquisicion', 'kilometraje', 'personal']

class MantencionForm(forms.ModelForm):
    class Meta:
        model = MantencionVehiculos
        fields = ['vehiculo', 'fecha_mantencion', 'kilometraje', 'valor', 'detalles']

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['primer_nombre',
                  'segundo_nombre', 
                  'apellido_paterno', 
                  'apellido_materno', 
                  'rut', 
                  'fecha_nacimiento', 
                  'nacionalidad',
                  'sexo', 
                  'telefono',
                  'correo', 
                  'direccion',
                  'comuna',
                  'afp', 
                  'salud', 
                  'estado_civil',
                  'talla_pantalon',
                  'talla_zapato',
                  'talla_torso', 
                  'sueldo_base',
                  'bono_colacion',
                  'bono_movilizacion',
                  'cargo',
                  'fecha_ingreso',
                  'supervisor',
                  'fecha_salida'
                  ]
        
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyectos
        fields = ['nombre',
                  'descripcion', 
                  'ubicacion', 
                  'fecha_inicio', 
                  'fecha_fin', 
                  'plazo', 
                  'monto_presupuesto',
                  'cliente',
                  'encargado',
                  'proyecto_serviu',
                  'id_proyecto_serviu',
                  'estado'
                  ]

class AnalisisForm(forms.ModelForm):
    class Meta:
        model = AnalisisPreciosUnitarios
        fields = ['nombre']

class MaterialCostForm(forms.ModelForm):
    class Meta:
        model = MaterialCost
        fields = ['material', 'cantidad', 'precio_unitario']

class LaborCostForm(forms.ModelForm):
    class Meta:
        model = LaborCost
        fields = ['descripcion', 'rendimiento', 'monto']

class EquipmentCostForm(forms.ModelForm):
    class Meta:
        model = EquipmentCost
        fields = ['descripcion', 'rendimiento', 'monto']

