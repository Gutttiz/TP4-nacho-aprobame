from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comentario
from .forms import ComentarioForm

def post_list(request):
    posts = Post.objects.order_by('-creado')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.filter(padre__isnull=True).order_by('-creado')

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        padre_id = request.POST.get('padre_id')
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            if padre_id:
                comentario.padre = Comentario.objects.get(id=padre_id)
            comentario.save()
            return redirect('blog:post_detail', pk=post.pk)  # ✅ Corregido
    else:
        form = ComentarioForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form
    })

from .forms import PostForm

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # Devuelve la lista de posts actualizada
                posts = Post.objects.all().order_by('-creado')
                return render(request, 'blog/post_list.html', {'posts': posts})
            return redirect('blog:post_list')  # ✅ Cambiado de 'blog:index' a 'blog:post_list'
    else:
        form = PostForm()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'blog/crear_post.html', {'form': form})
    return render(request, 'blog/crear_post.html', {'form': form})
