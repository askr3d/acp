from django.shortcuts import render, redirect
from .models import Afiliado, Usuario, Post
from django.core.mail import EmailMessage
from .forms import RegistroUsuarioForm


# Create your views here.

# RETRIEVING HTML FILES

# SITIO PRINCIPAL

def index(request):
    return render(request=request, template_name="asociacion/index.html")


def blog(request):
    return render(request=request, template_name="asociacion/blog.html")


# CRUD
def iniciar_sesion_view(request):
    return render(request=request, template_name='crud/login.html')


def crear_posts_view(request):
    return render(request=request, template_name='crud/new_post.html')


def iniciar_sesion(request):
    if request.method == 'POST' and request.POST:
        usuario = request.POST.get('usuario')
        contrasenia = request.POST.get('contrasenia')

        usuario_db = Usuario.objects.get(username=usuario, contrasenia=contrasenia)

        if usuario_db.username == usuario and usuario_db.contrasenia == contrasenia:
            return render(request, template_name="crud/admin_usuarios.html",  context={'usuarios': Usuario.objects.all(), 'form': RegistroUsuarioForm()})

        return redirect('iniciar_sesion')


def mostrar_usuarios(request):
    return render(request=request, template_name="crud/admin_usuarios.html",
                  context={'usuarios': Usuario.objects.all(), 'form': RegistroUsuarioForm()})


def mostrar_posts(request):
    return render(request=request, template_name="crud/admin_posts.html",
                  context={'posts': Post.objects.all()})



# QUERIES
def agregar_afiliado(request):
    if request.POST:
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        folio = request.POST.get("folio")
        corporacion = request.POST.get("corporacion")
        telefono = request.POST.get("telefono")
        nombramiento = request.POST.get("nombramiento")
        comentarios = request.POST.get("comentarios")

        afiliado = Afiliado.objects.create(nombre=nombre, email=email,
                                           folio_credencial=folio, corporacion=corporacion,
                                           telefono=telefono, nombramiento=nombramiento,
                                           comentarios=comentarios)

        return render(request=request, template_name="asociacion/index.html")

    else:
        return redirect('inicio')


# QUERIES USUARIO

def agregarUsuario(request):
    if request.POST:
        nombre = request.POST.get("nombre")
        username = request.POST.get("username")
        contrasenia = request.POST.get("contrasenia")

        usuario = Usuario.objects.create(nombre=nombre, username=username, contrasenia=contrasenia)

        return render(request=request, template_name="crud/admin_usuarios.html",
                      context={'usuarios': Usuario.objects.all(), 'form': RegistroUsuarioForm()})
    else:
        return redirect('mostrar_usuarios')


def eliminar_usuario(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    usuario.delete()

    return render(request=request, template_name="crud/admin_usuarios.html",
                  context={'usuarios': Usuario.objects.all()})



# QUERIES POSTS

