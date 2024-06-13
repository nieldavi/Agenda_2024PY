from django import forms
from apps.contatos.models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('usuario',)
        labels = {
            'nome': 'Nome',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'endereco': 'Endereço',
            'imagem': 'Imagem',
        }
        wigtes = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            
        }
