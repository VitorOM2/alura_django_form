"""
Módulo onde para a configuração das views relacionadas a passagens
index - Página com formulário da passagem
minha_consulta - Página que exibe os dados do formulário
"""
from django.shortcuts import render
from passagens.forms import PassagemForms,PessoaForms


def index(request):
    """ Configura a view index """
    form = PassagemForms()
    pessoa_form = PessoaForms()
    contexto = {'form':form, 'pessoa_form':pessoa_form}
    return render(request, 'index.html', contexto)

def minha_consulta(request):
    """ Exibe os dados do formulários """
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        pessoa_form = PessoaForms(request.POST)
        contexto = {'form':form, 'pessoa_form':pessoa_form}
        if form.is_valid():
            return render(request, 'minha_consulta.html', contexto)
        return render(request, 'index.html', contexto)
    contexto = {'form':form, 'pessoa_form':pessoa_form}
    return render(request, 'index.html', contexto)
