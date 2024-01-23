# Generated by Django 3.2.23 on 2024-01-23 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bibliotecaapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentarios',
            name='tipoComentario',
        ),
        migrations.AddField(
            model_name='comentarios',
            name='libro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bibliotecaapp.libros'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleados',
            name='IDcargo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bibliotecaapp.cargos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historialvisitas',
            name='id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libros',
            name='IDautor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bibliotecaapp.autores'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libros',
            name='IDeditorial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bibliotecaapp.editoriales'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libros',
            name='IDgenero',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bibliotecaapp.generos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='penalizaciones',
            name='IDprestamo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bibliotecaapp.prestamos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='penalizaciones',
            name='IDtipoPenalizacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bibliotecaapp.tipopenalizaciones'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prestamorecursos',
            name='IDempleado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bibliotecaapp.empleados'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prestamorecursos',
            name='IDrecurso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bibliotecaapp.recursostecnologicos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prestamorecursos',
            name='id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prestamos',
            name='IDempleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bibliotecaapp.empleados'),
        ),
        migrations.AddField(
            model_name='prestamos',
            name='IDlibro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bibliotecaapp.libros'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prestamos',
            name='id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservas',
            name='id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='reservasUsuarios',
            fields=[
                ('IDreservaUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150, null=True)),
                ('fechaReserva', models.DateTimeField(auto_now_add=True)),
                ('fechaRetiro', models.DateTimeField()),
                ('IDlibro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotecaapp.libros')),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
