# Generated by Django 4.2.5 on 2023-12-06 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='autores',
            fields=[
                ('IDautor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=70)),
                ('sexo', models.CharField(max_length=1)),
                ('fechaNacimiento', models.DateField()),
                ('alias', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='cargos',
            fields=[
                ('IDcargo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='comentarios',
            fields=[
                ('IDcomentario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('tipoComentario', models.CharField(max_length=10)),
                ('comentario', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('IDcontacto', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCompleto', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=25)),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='editoriales',
            fields=[
                ('IDeditorial', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=300)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='empleados',
            fields=[
                ('IDempleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=300)),
                ('documentoIdentidad', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=20)),
                ('fechaContratacion', models.DateField(auto_now_add=True)),
                ('estado', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='generos',
            fields=[
                ('IDgenero', models.AutoField(primary_key=True, serialize=False)),
                ('nombreGenero', models.CharField(max_length=70)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='historialVisitas',
            fields=[
                ('IDvisita', models.AutoField(primary_key=True, serialize=False)),
                ('salida', models.TimeField(null=True)),
                ('entrada', models.DateTimeField(auto_now_add=True)),
                ('presencial', models.SmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='libros',
            fields=[
                ('IDlibro', models.IntegerField(primary_key=True, serialize=False)),
                ('ISBN', models.IntegerField()),
                ('titulo', models.CharField(max_length=255)),
                ('portada', models.URLField(null=True)),
                ('descripcion', models.TextField(null=True)),
                ('fechaPublicacion', models.IntegerField()),
                ('edicion', models.CharField(max_length=50, null=True)),
                ('existencias', models.IntegerField()),
                ('sinopsis', models.TextField(null=True)),
                ('paginas', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='penalizaciones',
            fields=[
                ('IDpenalizacion', models.AutoField(primary_key=True, serialize=False)),
                ('estadoPenalizacion', models.SmallIntegerField()),
                ('detalle', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='prestamoRecursos',
            fields=[
                ('IDprestamoRecurso', models.AutoField(primary_key=True, serialize=False)),
                ('inicio', models.DateTimeField(auto_now_add=True)),
                ('salida', models.DateTimeField()),
                ('detalle', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='prestamos',
            fields=[
                ('IDprestamo', models.AutoField(primary_key=True, serialize=False)),
                ('fechaSalida', models.DateTimeField(auto_now_add=True)),
                ('fechaEntrada', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='recursosTecnologicos',
            fields=[
                ('IDrecurso', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=150)),
                ('ubicacion', models.CharField(max_length=200)),
                ('estadoEquipo', models.CharField(max_length=200)),
                ('estado', models.SmallIntegerField()),
                ('marca', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='tipoPenalizaciones',
            fields=[
                ('IDtipoPenalizacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('IDusuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=300)),
                ('telefono', models.CharField(max_length=12)),
                ('documentoIdentidad', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=255, unique=True)),
                ('fechaRegistro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='reseñas',
            fields=[
                ('IDreseña', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.TextField()),
                ('puntuacion', models.DecimalField(decimal_places=2, max_digits=3)),
                ('IDprestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotecaapp.prestamos')),
            ],
        ),
        migrations.CreateModel(
            name='reservas',
            fields=[
                ('IDreserva', models.AutoField(primary_key=True, serialize=False)),
                ('fechaReserva', models.DateTimeField(auto_now_add=True)),
                ('fechaRetiro', models.DateTimeField()),
                ('estado', models.SmallIntegerField()),
                ('IDlibro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotecaapp.libros')),
            ],
        ),
    ]