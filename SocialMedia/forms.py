from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        labels = {
            'content': 'Contenido',        
        }
        
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']  # Especifica los campos que deseas permitir editar
        labels = {
            'content': 'Contenido',
        }
    def __init__(self, *args, **kwargs):
        super(EditPostForm, self).__init__(*args, **kwargs)
        # Personaliza los widgets o agrega clases CSS aquí si es necesario
