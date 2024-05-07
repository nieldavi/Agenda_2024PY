from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path

# Create your views here.

# Create your views here.
def index(request):
    return render(request, 'contatos/index.html')

def contato(resquest):
    return render(resquest, 'contatos/det_contato.html')

