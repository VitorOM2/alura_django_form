from django.shortcuts import render
from passagens.forms import PassagemForms


def index(request):
    """ Configura a view index """
    form = PassagemForms()
    contexto = {'form':form}
    return render(request, 'index.html', contexto)

def minha_consulta(request):
    """ Exibe os dados do formulários """
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        contexto = {'form':form}
        return render(request, 'minha_consulta.html', contexto)