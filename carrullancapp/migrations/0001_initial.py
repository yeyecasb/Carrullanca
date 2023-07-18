# Generated by Django 4.2.3 on 2023-07-12 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AFP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('porcentaje_cotizacion', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('apellido', models.CharField(blank=True, max_length=100, null=True)),
                ('razon_social', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=10)),
                ('nombre_representante', models.CharField(blank=True, max_length=100, null=True)),
                ('rut_representante', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=255)),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EGR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=10)),
                ('representante', models.CharField(max_length=100)),
                ('rut_representante', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materiales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('unidad_medida', models.CharField(max_length=10)),
                ('costo_unitario', models.IntegerField()),
                ('peso_material', models.IntegerField()),
                ('volumen_material', models.IntegerField()),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=50)),
                ('segundo_nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=10)),
                ('fecha_nacimiento', models.DateField()),
                ('nacionalidad', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=50)),
                ('talla_pantalon', models.IntegerField(blank=True, null=True)),
                ('talla_zapato', models.IntegerField(blank=True, null=True)),
                ('talla_torso', models.IntegerField(blank=True, null=True)),
                ('sueldo_base', models.IntegerField()),
                ('bono_colacion', models.IntegerField()),
                ('bono_movilizacion', models.IntegerField()),
                ('cargo', models.CharField(max_length=50)),
                ('fecha_ingreso', models.DateField()),
                ('fecha_salida', models.DateField()),
                ('estado', models.BooleanField()),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
                ('afp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.afp')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=10)),
                ('producto', models.CharField(max_length=100)),
                ('linea_credito', models.IntegerField(blank=True, null=True)),
                ('credito_utilizado', models.IntegerField(blank=True, null=True)),
                ('plazo_pago', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=255)),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255)),
                ('ubicacion', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('plazo', models.IntegerField()),
                ('monto_presupuesto', models.IntegerField()),
                ('proyecto_serviu', models.BooleanField()),
                ('id_proyecto_serviu', models.IntegerField()),
                ('estado', models.BooleanField()),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.clientes')),
                ('encargado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.personal')),
            ],
        ),
        migrations.CreateModel(
            name='Salud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('porcentaje_cotizacion', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subcontratistas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=10)),
                ('especialidad', models.CharField(max_length=50)),
                ('contacto', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.IntegerField()),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=7)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('serie_motor', models.CharField(max_length=50)),
                ('serie_chasis', models.CharField(max_length=50)),
                ('año', models.IntegerField()),
                ('categoria', models.CharField(max_length=50)),
                ('combustible', models.CharField(max_length=15)),
                ('fecha_adquisicion', models.DateField()),
                ('km_adquisicion', models.IntegerField()),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.personal')),
            ],
        ),
        migrations.CreateModel(
            name='SubcontratistasPorProyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.proyectos')),
                ('subcontratista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.subcontratistas')),
            ],
        ),
        migrations.CreateModel(
            name='ProyectoMAVEServiu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_ingreso', models.DateField()),
                ('codigo_postulacion', models.IntegerField()),
                ('Localidad', models.CharField(max_length=50)),
                ('nombre_beneficiario', models.CharField(max_length=100)),
                ('apellido_paterno_beneficiario', models.CharField(max_length=100)),
                ('apellido_materno_beneficiario', models.CharField(max_length=100)),
                ('rut_beneficiario', models.CharField(max_length=10)),
                ('nombre_conyuge', models.CharField(max_length=100)),
                ('apellido_paterno_conyuge', models.CharField(max_length=100)),
                ('apellido_materno_conyuge', models.CharField(max_length=100)),
                ('rut_conyuge', models.CharField(max_length=10)),
                ('deficit', models.CharField(max_length=10)),
                ('postulante_adulto_mayor', models.BooleanField()),
                ('integrantes_familia', models.IntegerField()),
                ('integrante_adulto_mayor', models.BooleanField()),
                ('factor_multiplicador', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipologia_1', models.CharField(max_length=50)),
                ('tipologia_2', models.CharField(max_length=50)),
                ('tipologia_3', models.CharField(max_length=50)),
                ('subsidio_1', models.IntegerField()),
                ('subsidio_2', models.IntegerField()),
                ('subsidio_3', models.IntegerField()),
                ('regularizacion', models.IntegerField()),
                ('discapacidad', models.IntegerField()),
                ('ahorro', models.IntegerField()),
                ('ahorro_exento', models.IntegerField()),
                ('descripcion', models.CharField(max_length=255)),
                ('ubicacion', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('plazo', models.IntegerField()),
                ('monto_presupuesto', models.IntegerField()),
                ('estado', models.BooleanField()),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.clientes')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.comuna')),
                ('egr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.egr')),
                ('encargado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.personal')),
            ],
        ),
        migrations.CreateModel(
            name='Presupuestos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo_estimado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('costo_real', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_creacion', models.DateField()),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.proyectos')),
            ],
        ),
        migrations.AddField(
            model_name='personal',
            name='salud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.salud'),
        ),
        migrations.AddField(
            model_name='personal',
            name='supervisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='carrullancapp.personal'),
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_pago', models.DateField()),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.proveedores')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenesCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('fecha_orden', models.DateField()),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.materiales')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialesPorProyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.materiales')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.proyectos')),
            ],
        ),
        migrations.AddField(
            model_name='materiales',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.proveedores'),
        ),
        migrations.CreateModel(
            name='MantencionVehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_mantencion', models.DateField()),
                ('kilometraje', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('detalles', models.CharField(max_length=255)),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.vehiculos')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_actual', models.IntegerField()),
                ('ubicacion_inventario', models.CharField(max_length=255)),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.materiales')),
            ],
        ),
        migrations.CreateModel(
            name='HorasTrabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('horas_trabajadas', models.IntegerField()),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.personal')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.proyectos')),
            ],
        ),
        migrations.CreateModel(
            name='Factoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_factoring', models.DateField()),
                ('monto', models.IntegerField()),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.proyectos')),
            ],
        ),
        migrations.CreateModel(
            name='ControlObras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.proyectos')),
            ],
        ),
        migrations.CreateModel(
            name='AnalisisPreciosUnitarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_modificacion', models.DateField(auto_now_add=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrullancapp.materiales')),
            ],
        ),
    ]
