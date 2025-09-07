# forms.py
from django import forms
from .models import Comentario, Post

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'contenido']
        widgets = {
            'autor': forms.TextInput(attrs={
                'placeholder': 'Tu nombre',
                'class': 'input-com',
                'pattern': '[A-Za-zÁÉÍÓÚáéíóúÑñ\\s]{1,100}'
            }),
            'contenido': forms.Textarea(attrs={
                'placeholder': 'Tu comentario...',
                'rows': 3,
                'class': 'textarea-com',
                'maxlength': '300'
            }),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen', 'max_comentarios']  # ya incluye max_comentarios
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del post'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribí el contenido'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'max_comentarios': forms.NumberInput(attrs={'class': 'form-control', 'value': 100, 'min': 1, 'max': 500}),
        }
