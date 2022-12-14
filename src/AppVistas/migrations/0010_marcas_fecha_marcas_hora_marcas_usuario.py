# Generated by Django 4.0.6 on 2022-09-05 02:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppVistas', '0009_remove_proveedores_fecha_remove_proveedores_hora'),
    ]

    operations = [
        migrations.AddField(
            model_name='marcas',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marcas',
            name='hora',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marcas',
            name='usuario',
            field=models.CharField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
    ]
