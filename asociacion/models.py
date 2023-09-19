from django.db import models


# Create your models here.
class Afiliado(models.Model):
    # Extiende la clase AbstractUser por defecto de Django...

    nombre = models.CharField(
        unique=True,
        error_messages={
            'unique': 'Nombre de usuario no disponible.'
        }, max_length=50)
    # redefinimos el field email de la clase usser para validar que el email sea unico.
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'Esta dirección de correo electrónico ya está siendo usada por otra cuenta.'
        }
    )
    # folio de credencial de elector.
    folio_credencial = models.CharField(
        unique=True,
        error_messages={
            'unique': 'Este folio ya está siendo usado por otra cuenta.'
        }, max_length=18)

    # corporacion a la que se pertence
    corporacion = models.CharField(max_length=18)

    telefono = models.CharField(max_length=10)

    nombramiento = models.CharField(max_length=30)

    comentarios = models.TextField(max_length=100)


class Usuario(models.Model):
    #username
    username = models.CharField(
        unique=True,
        error_messages={
            'unique': 'Nombre de usuario no disponible.'
        }, max_length=50)

    #nombre completo del usuario
    nombre = models.CharField(unique=True, max_length=40)
    contrasenia = models.CharField(unique=True, max_length=40)


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField(max_length=2000)
    imagen = models.ImageField(upload_to='uploads/', null=False, default="")

    #creador es necesario pasarle el id de un usuario existente, CASCADE para que si se elimina el usuario se eliminen sus post

    usuario_creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
