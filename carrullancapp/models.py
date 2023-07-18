from django.db import models


# , null=True
#, blank=True
# Create your models here.
class AFP(models.Model):
    nombre = models.CharField(max_length=100)
    porcentaje_cotizacion = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Salud(models.Model):
    nombre = models.CharField(max_length=100)
    porcentaje_cotizacion = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class EGR(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    representante = models.CharField(max_length=100)
    rut_representante = models.CharField(max_length=10)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField()
    email = models.EmailField()
    fecha_modificacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Clientes(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    razon_social = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    nombre_representante = models.CharField(max_length=100, null=True, blank=True)
    rut_representante = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=255)
    fecha_modificacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.razon_social

class Proveedores(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    producto = models.CharField(max_length=100)
    linea_credito = models.IntegerField(null=True, blank=True)
    credito_utilizado = models.IntegerField(null=True, blank=True)
    plazo_pago = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=255)
    fecha_modificacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Personal(models.Model):
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, null=True, blank=True)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.EmailField()
    direccion = models.CharField(max_length=50)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=True, blank=True)
    afp = models.ForeignKey(AFP, on_delete=models.CASCADE)
    salud = models.ForeignKey(Salud, on_delete=models.CASCADE)
    estado_civil = models.CharField(max_length=50)
    talla_pantalon= models.IntegerField(null=True, blank=True)
    talla_zapato = models.IntegerField(null=True, blank=True)
    talla_torso = models.IntegerField(null=True, blank=True)
    sueldo_base = models.IntegerField(null=True, blank=True)
    bono_colacion = models.IntegerField( null=True, blank=True)
    bono_movilizacion = models.IntegerField( null=True, blank=True)
    cargo = models.CharField(max_length=50, null=True, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    fecha_salida = models.DateField(null=True, blank=True)
    estado = models.BooleanField(null=True, blank=True)
    fecha_modificacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.primer_nombre + " " + self.apellido_paterno
    
class Vehiculos(models.Model):
    patente = models.CharField(max_length=7)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serie_motor = models.CharField(max_length=50, null=True, blank=True)
    serie_chasis = models.CharField(max_length=50, null=True, blank=True)
    año = models.IntegerField()
    categoria = models.CharField(max_length=50)
    combustible = models.CharField(max_length=15)
    fecha_adquisicion = models.DateField()
    km_adquisicion = models.IntegerField()  
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    kilometraje = models.IntegerField(null=True, blank=True)
    fecha_modificacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.patente

class MantencionVehiculos(models.Model):
    vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
    fecha_mantencion = models.DateField()
    kilometraje = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    detalles = models.CharField(max_length=255)
    fecha_modificacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.vehiculo.patente

class Materiales(models.Model):
    nombre = models.CharField(max_length=100)
    unidad_medida = models.CharField(max_length=10)
    costo_unitario = models.IntegerField()
    peso_material = models.IntegerField()
    volumen_material = models.IntegerField()
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    fecha_modificacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Proyectos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    plazo = models.IntegerField()
    monto_presupuesto = models.IntegerField()
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    encargado = models.ForeignKey(Personal, on_delete=models.CASCADE)
    proyecto_serviu =models.BooleanField()
    id_proyecto_serviu = models.IntegerField()
    estado = models.BooleanField()
    fecha_modificacion = models.DateField(auto_now_add=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    presupues


    def __str__(self):
        return self.nombre

class SubProyectoMAVEServiu(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    codigo_postulacion = models.IntegerField()
    Localidad = models.CharField(max_length=50)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    egr = models.ForeignKey(EGR, on_delete=models.CASCADE)
    nombre_beneficiario = models.CharField(max_length=100)
    apellido_paterno_beneficiario = models.CharField(max_length=100)
    apellido_materno_beneficiario = models.CharField(max_length=100)
    rut_beneficiario = models.CharField(max_length=10)
    nombre_conyuge = models.CharField(max_length=100)
    apellido_paterno_conyuge = models.CharField(max_length=100)
    apellido_materno_conyuge = models.CharField(max_length=100)
    rut_conyuge = models.CharField(max_length=10)
    deficit = models.CharField(max_length=10)
    postulante_adulto_mayor = models.BooleanField()
    integrantes_familia = models.IntegerField()
    integrante_adulto_mayor = models.BooleanField()
    factor_multiplicador = models.DecimalField(max_digits=10, decimal_places=2)
    tipologia_1 = models.CharField(max_length=50)
    tipologia_2 = models.CharField(max_length=50)
    tipologia_3 = models.CharField(max_length=50)
    subsidio_1 = models.IntegerField()
    subsidio_2 = models.IntegerField()
    subsidio_3 = models.IntegerField()
    regularizacion = models.IntegerField()
    discapacidad = models.IntegerField()
    ahorro = models.IntegerField()
    ahorro_exento = models.IntegerField()
    descripcion = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    plazo = models.IntegerField()
    monto_presupuesto = models.IntegerField()
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    encargado = models.ForeignKey(Personal, on_delete=models.CASCADE)
    estado = models.BooleanField()
    fecha_modificacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class MaterialesPorProyecto(models.Model):
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    material = models.ManyToManyField(Materiales)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.proyecto.nombre

class Subcontratistas(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    especialidad = models.CharField(max_length=50)
    contacto = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField()
    fecha_modificacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class SubcontratistasPorProyectos(models.Model):
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    subcontratista = models.ManyToManyField(Subcontratistas)

    def __str__(self):
        return self.proyecto.nombre

class Factoring(models.Model):
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    nombre_factoring = models.CharField(max_length=100, null=True, blank=True)
    rut_factoring = models.CharField(max_length=10, null=True, blank=True)
    n_factura = models.IntegerField(null=True, blank=True)    
    fecha_factoring = models.DateField(null=True, blank=True)
    monto = models.IntegerField(null=True, blank=True)
    fecha_modificacion = models.DateField(auto_now_add=True)
    estado = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.nombre_factoring

class OrdenesCompra(models.Model):
    material = models.ForeignKey(Materiales, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    fecha_orden = models.DateField()
    fecha_modificacion = models.DateField(auto_now_add=True)

class Inventario(models.Model):
    material = models.ForeignKey(Materiales, on_delete=models.CASCADE)
    cantidad_actual = models.IntegerField()
    ubicacion_inventario = models.CharField(max_length=255)
    fecha_modificacion = models.DateField(auto_now_add=True)

class HorasTrabajo(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    fecha = models.DateField()
    horas_trabajadas = models.IntegerField()
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    fecha_modificacion = models.DateField(auto_now_add=True)

class Pagos(models.Model):
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    fecha_modificacion = models.DateField(auto_now_add=True)

class Presupuestos(models.Model):
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    costo_real = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField(auto_now_add=True)

class AnalisisPreciosUnitarios(models.Model):
    material = models.ForeignKey(Materiales, on_delete=models.CASCADE)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_modificacion = models.DateField(auto_now_add=True)

class ControlObras(models.Model):
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fecha_modificacion = models.DateField(auto_now_add=True)