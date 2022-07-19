# Generated by Django 4.0.4 on 2022-07-19 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('falla', '0001_initial'),
        ('equipo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProyectoEquiposFallas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipo.equipo')),
                ('falla_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='falla.falla')),
                ('proyecto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.proyecto')),
            ],
        ),
    ]
