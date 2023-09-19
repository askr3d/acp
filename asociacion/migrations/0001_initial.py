# Generated by Django 4.1.3 on 2022-12-01 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afiliado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(error_messages={'unique': 'Nombre de usuario no disponible.'}, max_length=50, unique=True)),
                ('email', models.EmailField(error_messages={'unique': 'Esta dirección de correo electrónico ya está siendo usada por otra cuenta.'}, max_length=254, unique=True)),
                ('folio_credencial', models.CharField(error_messages={'unique': 'Este folio ya está siendo usado por otra cuenta.'}, max_length=18, unique=True)),
                ('corporacion', models.CharField(max_length=18)),
                ('telefono', models.CharField(max_length=10)),
                ('nombramiento', models.CharField(max_length=30)),
                ('comentarios', models.TextField(max_length=100)),
            ],
        ),
    ]