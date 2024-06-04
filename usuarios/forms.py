from django import forms

class LoginForms(forms.Form):
    username = forms.CharField(label= 'Nome de login',
                               required = True,widget = forms.TextInput(
                                   attrs={"class": "form-control",
                                          "placeholder": "Digite seu nome de login"}
                               ),
                               max_length = 100)
    password = forms.CharField(label= 'senha',
                               required= True,
                               widget = forms.PasswordInput(
                                   attrs={"class": "form-control",
                                          "placeholder": "Digite sua senha"}
                               ),
                               max_length = 100)
    
class CadastroForms(forms.Form):
    username = forms.CharField(label= 'Nome de login',
                               required = True,
                               widget = forms.TextInput(
                                   attrs={"class": "form-control",
                                          "placeholder": "Digite seu nome de login"}
                               ),
                               max_length = 100)
    email = forms.EmailField(label= 'Email',
                             required=True,
                             max_length = 100,
                             widget=forms.EmailInput(
                                    attrs={"class":"form-control",
                                            "placeholder":"Digite seu email"}
                                ),
                             )
    senha_1 = forms.CharField(label= 'senha',
                               required= True,
                               widget = forms.PasswordInput(
                                   attrs={"class": "form-control",
                                          "placeholder": "Digite sua senha"}
                               ),
                               max_length = 100)
    senha_2 = forms.CharField(label= 'Confirme sua senha',
                               required= True,
                               widget = forms.PasswordInput(
                                   attrs={"class": "form-control",
                                          "placeholder": "Digite sua senha novamente"}
                               ),
                               max_length = 100)