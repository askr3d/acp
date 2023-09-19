from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('blog/', views.blog, name='blog'),
    path('agregar_afiliado/', views.agregar_afiliado, name='agregar_afiliado'),
    path('administrar_usuarios/', views.mostrar_usuarios, name='mostrar_usuarios'),
    path('agregarUsuario/', views.agregarUsuario, name="agregarUsuario"),
    path('eliminar_usuario/<int:id_usuario>', views.eliminar_usuario, name='eliminar_usuario'),
    path('administrarPosts/', views.mostrar_posts, name='mostrar_posts'),
    path('iniciarSesionView/', views.iniciar_sesion_view, name='iniciar_sesion_view'),
    path('iniciarSesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('agregarPostView', views.crear_posts_view, name='crear_post_view')
]
