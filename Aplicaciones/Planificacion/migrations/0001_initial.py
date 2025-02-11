# Generated by Django 5.1.6 on 2025-02-06 02:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Constructora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.TextField()),
                ('tipo', models.CharField(max_length=100)),
                ('metros_cuadrados', models.FloatField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(choices=[('En construcción', 'En construcción'), ('Terminada', 'Terminada')], max_length=50)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Planificacion.cliente')),
                ('constructora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Planificacion.constructora')),
            ],
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En progreso', 'En progreso'), ('Finalizada', 'Finalizada')], max_length=50)),
                ('vivienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Planificacion.vivienda')),
            ],
        ),
    ]
