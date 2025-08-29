from django import forms
from .models import Comentario
from .models import Post

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'contenido']
        widgets = {
            'autor': forms.TextInput(attrs={'placeholder': 'Tu nombre', 'class': 'input-com'}),
            'contenido': forms.Textarea(attrs={'placeholder': 'Tu comentario...', 'rows': 3, 'class': 'textarea-com'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del post'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribí el contenido'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

