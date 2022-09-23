from django.shortcuts import render
from passagens.forms import PassagemForms


def index(request):
    """ Configura a view index """
    form = PassagemForms()
    contexto = {'form':form}
    return render(request, 'index.html', contexto)
