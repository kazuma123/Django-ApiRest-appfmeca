# Generated by Django 4.0.4 on 2022-06-03 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0002_remove_area_proyecto_area_proyecto'),
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='area',
        ),
        migrations.AddField(
            model_name='equipo',
            name='area',
            field=models.ManyToManyField(to='area.area'),
        ),
    ]