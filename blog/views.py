from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .models import Post, Comentario
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all().order_by('-creado')
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'blog/post_list.html', {'posts': posts})
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    puede_comentar = post.puede_comentar()
    
    # Manejo simple de comentarios
    if request.method == 'POST' and puede_comentar:
        autor = request.POST.get('autor', '').strip()
        contenido = request.POST.get('contenido', '').strip()
        
        if autor and contenido:
            Comentario.objects.create(
                post=post,
                autor=autor,
                contenido=contenido
            )
            messages.success(request, '¡Comentario agregado!')
            return redirect('blog:post_detail', pk=pk)
        else:
            messages.error(request, 'Complete todos los campos.')
    elif request.method == 'POST' and not puede_comentar:
        messages.error(request, f'Post con límite de {post.max_comentarios} comentarios alcanzado.')
    
    context = {
        'post': post,
        'puede_comentar': puede_comentar,
        'total_comentarios': post.total_comentarios(),
        'max_comentarios': post.max_comentarios,
    }
    return render(request, 'blog/post_detail.html', context)

# CAMBIAR TODA ESTA FUNCIÓN:
def crear_post(request):
    # VERIFICACIÓN COMPLETA: debe estar logueado Y ser admin
    if not request.user.is_authenticated:
        messages.error(request, 'Debes iniciar sesión para crear posts.')
        return redirect('blog:post_list')  # O redirigir a login si tienes
    
    if not (request.user.is_superuser or request.user.is_staff):
        messages.error(request, 'Solo administradores pueden crear posts.')
        return redirect('blog:post_list')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Post creado exitosamente!')
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                posts = Post.objects.all().order_by('-creado')
                return render(request, 'blog/post_list.html', {'posts': posts})
            return redirect('blog:post_list')
        else:
            messages.error(request, 'Error al crear el post. Revisa los campos.')
    else:
        form = PostForm()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'blog/crear_post.html', {'form': form})
    return render(request, 'blog/crear_post.html', {'form': form})

@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def delete_post(request, pk):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=pk)
        post.delete()
    return redirect("blog:post_list")

@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def delete_comment(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    post_id = comentario.post.pk  # Para redirigir al post original
    if request.method == "POST":
        comentario.delete()
    return redirect("blog:post_detail", pk=post_id)