# Generated by Django 4.0.6 on 2022-09-02 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppVistas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('ubicacion', models.CharField(max_length=30)),
            ],
        ),
    ]
