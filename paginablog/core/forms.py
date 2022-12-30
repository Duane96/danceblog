from django import forms
from .models import Comentarios

class EmailPostForm(forms.Form):
    nombre= forms.CharField(max_length=25, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class':'form-control'}
    ))
    para = forms.EmailField(widget=forms.EmailInput(
        attrs={'class':'form-control'}
    ))
    comentario = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class':'form-area'}
    ))
    
    


class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ('nombre', 'email', 'body')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-area'}),
        }
        labels = {
            'body': ('Comentario'),
        }
    