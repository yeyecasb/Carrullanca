from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculos, MantencionVehiculos, Personal
from .forms import VehiculoForm, MantencionForm, PersonalForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Listar todas las manutenciones
def listado_vehiculos(request):
    vehiculos = Vehiculos.objects.all()
    return render(request, 'vehiculos.html', {'vehiculos': vehiculos})


def nuevo_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'editar_vehiculo.html', {'form': form})

# Editar un vehículo existente
def editar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculos, pk=id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('vehiculos')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'editar_vehiculo.html', {'form': form})

#Eliminar un Vehiculo
def eliminar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculos, pk=id)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('vehiculos')
    return render(request, 'eliminar_vehiculo.html', {'vehiculo': vehiculo})

# Listar todas las manutenciones
def mantenciones(request):
    mantenciones = MantencionVehiculos.objects.all()
    return render(request, 'mantenciones.html', {'mantenciones': mantenciones})

# Crear una nueva manutención
def nueva_mantencion(request):
    if request.method == 'POST':
        form = MantencionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mantenciones')
    else:
        form = MantencionForm()
    return render(request, 'editar_mantencion.html', {'form': form})

# Editar una manutención existente
def editar_mantencion(request, id):
    mantencion = get_object_or_404(MantencionVehiculos, pk=id)
    if request.method == 'POST':
        form = MantencionForm(request.POST, instance=mantencion)
        if form.is_valid():
            form.save()
            return redirect('mantenciones')
    else:
        form = MantencionForm(instance=mantencion)
    return render(request, 'editar_mantencion.html', {'form': form})

# Eliminar una manutención
def eliminar_mantencion(request, id):
    mantencion = get_object_or_404(MantencionVehiculos, pk=id)
    if request.method == 'POST':
        mantencion.delete()
        return redirect('mantenciones')
    return render(request, 'eliminar_mantencion.html', {'mantencion': mantencion})

# Crear un nuevo registro de personal
def nuevo_personal(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal')
    else:
        form = PersonalForm()
    return render(request, 'editar_personal.html', {'form': form})

# Editar un registro de personal existente
def editar_personal(request, id):
    personal = get_object_or_404(Personal, pk=id)
    if request.method == 'POST':
        form = PersonalForm(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('personal')
    else:
        form = PersonalForm(instance=personal)
    return render(request, 'editar_personal.html', {'form': form})

#Listar todos los registros de personal
def lista_personal(request):
    personal = Personal.objects.all()
    return render(request, 'personal.html', {'personal': personal})

# Eliminar un registro de personal
def eliminar_personal(request, id):
    personal = get_object_or_404(Personal, pk=id)
    if request.method == 'POST':
        personal.delete()
        return redirect('personal')
    return render(request, 'eliminar_personal.html', {'personal': personal})