from django.shortcuts import render
from blog.models import Post  # Usar el modelo del blog

def home(request):
    posts = Post.objects.all().order_by('-creado')[:3]  # Solo los 3 más recientes
    return render(request, 'portfolio/index.html', {'posts': posts})

def portfolio(request):
    return render(request, 'portfolio/index.html')