# Generated by Django 4.0.6 on 2022-09-03 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppForo', '0006_foro_hora_alter_foro_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foro',
            name='hora',
        ),
    ]