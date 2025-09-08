# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'  # ✅ Define el namespace

urlpatterns = [
    path('', views.post_list, name='post_list'),           # Lista de posts
    path('<int:pk>/', views.post_detail, name='post_detail'), # Detalle de post
    path('crear/', views.crear_post, name='crear_post'),    # Crear post
    path("post/<int:pk>/delete/", views.delete_post, name="delete_post"),
    path('comentario/<int:pk>/delete/', views.delete_comment, name='delete_comment')  
]