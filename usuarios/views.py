from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms
# Create your views here.
def login(resquest):
    forms = LoginForms()
    return render(resquest, 'usuarios/login.html', {'form':forms})

def cadastrar(request):
    froms = CadastroForms()
    return render(request, 'usuarios/cadastrar.html', {'form':froms})

def logout(request):
    return render(request, 'usuarios/logout.html')