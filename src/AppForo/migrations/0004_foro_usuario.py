# Generated by Django 4.0.6 on 2022-09-03 03:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppForo', '0003_foro_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='foro',
            name='usuario',
            field=models.CharField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
    ]
