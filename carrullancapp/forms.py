from django import forms
from .models import Vehiculos, MantencionVehiculos, Personal

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculos
        fields = ['patente', 'marca', 'modelo', 'serie_motor', 'serie_chasis', 'año', 'categoria', 'combustible', 'fecha_adquisicion', 'km_adquisicion', 'kilometraje', 'personal']

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