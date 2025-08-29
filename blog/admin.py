from django.contrib import admin
from .models import Post, Comentario

class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 0
    fk_name = 'post'

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'creado')
    inlines = [ComentarioInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Comentario)
