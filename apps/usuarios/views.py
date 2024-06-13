from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.
def login(request):
    forms = LoginForms()
    if request.method == 'POST':
        forms = LoginForms(request.POST)
        if forms.is_valid():
            name = forms['username'].value()
            senha = forms['password'].value()
            user = auth.authenticate(request, 
                                    username=name, 
                                    password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login efetuado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Usuário ou senha inválidos!')
                return redirect('login')
    return render(request, 'usuarios/login.html', {'form':forms})

def cadastrar(request):
    forms = CadastroForms()

    if request.method == 'POST':
        forms = CadastroForms(request.POST)
        
        if forms.is_valid():
            if forms['senha_1'].value() != forms['senha_2'].value():
                messages.error(request, 'As senhas não conferem!')
                return redirect('cadastrar')
            name = forms['username'].value()
            email = forms['email'].value()
            senha = forms['senha_1'].value()

            if User.objects.filter(username=name).exists():
                messages.error(request, 'Nome de usuário já existe!')
                return redirect('cadastrar')
            usuario = User.objects.create_user(username=name, email=email, password=senha)
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login')
    return render(request, 'usuarios/cadastrar.html', {'form':forms})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Deslogado com sucesso!')
    return redirect('login')