from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path
from apps.contatos.models import Contato
from django.contrib import messages
from apps.contatos.forms import ContatoForm

# Create your views here.

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')
        return redirect('login')
    contatos = Contato.objects.filter(usuario = request.user)
    return render(request, 'contatos/index.html', {'conts': contatos} )

def contato(resquest,info_id):
    contato = get_object_or_404(Contato, pk =info_id)
    return render(resquest, 'contatos/det_contato.html', {'contato': contato})


def buscar(request):
    contatos = Contato.objects.filter(usuario = request.user)
    if 'buscar' in request.GET:
        nome = request.GET['buscar']
        if nome:
            contatos = Contato.objects.filter(nome__icontains=nome)
    return render(request, 'contatos/buscar.html', {'conts': contatos})

def novo_contato(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')
        return redirect('login')
    form =ContatoForm()
    if request.method == 'POST':
        form = ContatoForm(request.POST, request.FILES)
        if form.is_valid():
            contato  = form.save(commit=False)
            contato.usuario = request.user
            form.save()
            messages.success(request, 'Contato salvo com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao salvar contato!')
    return render(request, 'contatos/novo_contato.h)tml', {'form': form})


def editar_contato(request, info_id):
    contato = Contato.objects.get(pk=info_id)
    form = ContatoForm(instance=contato)
    if request.method == 'POST':
        form = ContatoForm(request.POST, request.FILES, instance=contato)   
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato alterado com sucesso!')
            redirect('index')
        else:
            messages.error(request, 'Erro ao alterar contato!')
    return render(request, 'contatos/editar_contato.html', {'form': form, 'info_id':info_id},)
def deletar_contato(request, info_id):
   contato = Contato.objects.get(pk=info_id)
   contato.delete()
   messages.success(request, 'Contato deletado com sucesso!')
   return redirect('index')  