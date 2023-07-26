from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculos, MantencionVehiculos, Personal, Proyectos, AnalisisPreciosUnitarios
from .forms import VehiculoForm, MantencionForm, PersonalForm, ProyectoForm, MaterialCostForm, LaborCostForm, EquipmentCostForm, AnalisisForm

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

# Crear proyecto
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'editar_proyecto.html', {'form': form})

# Listar proyectos
def lista_proyectos(request):
    proyectos = Proyectos.objects.all()
    return render(request, 'proyectos.html', {'proyectos': proyectos})

def editar_proyecto(request, id):
    proyecto = get_object_or_404(ProyectoForm, pk=id)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'editar_proyecto.html', {'form': form})

# Eliminar un registro de proyecto
def eliminar_proyecto(request, id):
    proyectos = get_object_or_404(Proyectos, pk=id)
    if request.method == 'POST':
        proyectos.delete()
        return redirect('proyectos')
    return render(request, 'eliminar_proyecto.html', {'proyectos': proyectos})

def material_cost_new(request, pk):
    analisis = get_object_or_404(AnalisisPreciosUnitarios, pk=pk)
    if request.method == "POST":
        form = MaterialCostForm(request.POST)
        if form.is_valid():
            material_cost = form.save(commit=False)
            material_cost.analisis = analisis
            material_cost.save()
            return redirect('analisis_detail', pk=analisis.pk)
    else:
        form = MaterialCostForm()
    return render(request, 'material_cost_edit.html', {'form': form})

def labor_cost_new(request, pk):
    analisis = get_object_or_404(AnalisisPreciosUnitarios, pk=pk)
    if request.method == "POST":
        form = LaborCostForm(request.POST)
        if form.is_valid():
            material_cost = form.save(commit=False)
            material_cost.analisis = analisis
            material_cost.save()
            return redirect('analisis_detail', pk=analisis.pk)
    else:
        form = LaborCostForm()
    return render(request, 'labor_cost_edit.html', {'form': form})

def equipament_cost_new(request, pk):
    analisis = get_object_or_404(AnalisisPreciosUnitarios, pk=pk)
    if request.method == "POST":
        form = EquipmentCostForm(request.POST)
        if form.is_valid():
            material_cost = form.save(commit=False)
            material_cost.analisis = analisis
            material_cost.save()
            return redirect('analisis_detail', pk=analisis.pk)
    else:
        form = EquipmentCostForm()
    return render(request, 'equipment_cost_edit.html', {'form': form})

def analisis_historial(request, pk):
    analisis = get_object_or_404(AnalisisPreciosUnitarios, pk=pk)
    costos_materiales = {costo.fecha: costo.total_cost for costo in analisis.material_costs.all()}
    costos_mano_de_obra = {costo.fecha: costo.total_cost for costo in analisis.labor_costs.all()}
    costos_equipos = {costo.fecha: costo.total_cost for costo in analisis.equipment_costs.all()}

    fechas = sorted(set(costos_materiales.keys()) | set(costos_mano_de_obra.keys()) | set(costos_equipos.keys()))

    costos_materiales_list = [costos_materiales.get(fecha, None) for fecha in fechas]
    costos_mano_de_obra_list = [costos_mano_de_obra.get(fecha, None) for fecha in fechas]
    costos_equipos_list = [costos_equipos.get(fecha, None) for fecha in fechas]

    return render(request, 'analisis_historial.html', {
        'analisis': analisis, 
        'fechas': fechas, 
        'costos_materiales': costos_materiales_list, 
        'costos_mano_de_obra': costos_mano_de_obra_list, 
        'costos_equipos': costos_equipos_list,
    })

def analisis_list(request):
    analisis_list = AnalisisPreciosUnitarios.objects.all()
    return render(request, 'analisis_list.html', {'analisis_list': analisis_list})

def analisis_new(request):
    if request.method == "POST":
        analisis_form = AnalisisForm(request.POST)
        material_form = MaterialCostForm(request.POST, prefix='material')
        labor_form = LaborCostForm(request.POST, prefix='labor')
        equipment_form = EquipmentCostForm(request.POST, prefix='equipment')

        if all([analisis_form.is_valid(), material_form.is_valid(), labor_form.is_valid(), equipment_form.is_valid()]):
            analisis = analisis_form.save()
            material_cost = material_form.save(commit=False)
            material_cost.analisis = analisis
            material_cost.save()
            labor_cost = labor_form.save(commit=False)
            labor_cost.analisis = analisis
            labor_cost.save()
            equipment_cost = equipment_form.save(commit=False)
            equipment_cost.analisis = analisis
            equipment_cost.save()
            return redirect('analisis_detail', pk=analisis.pk)
    else:
        analisis_form = AnalisisForm()
        material_form = MaterialCostForm(prefix='material')
        labor_form = LaborCostForm(prefix='labor')
        equipment_form = EquipmentCostForm(prefix='equipment')

    return render(request, 'analisis_edit.html', {
        'analisis_form': analisis_form, 
        'material_form': material_form, 
        'labor_form': labor_form, 
        'equipment_form': equipment_form,
    })