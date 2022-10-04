# pylint: disable=import-error
""" Módulo para a criação de formulários """
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe
from passagens.validation import *
from django import forms
from tempus_dominus.widgets import DatePicker


class PassagemForms(forms.Form):
    """ Cria o formulário de passagens """
    origem          = forms.CharField(label='Origem', max_length=100)
    destino         = forms.CharField(label='Destino', max_length=100)
    ida             = forms.DateField(label='Ida', widget=DatePicker())
    volta           = forms.DateField(label='Volta', widget=DatePicker())
    classe_viagem   = forms.ChoiceField(label='Classe do vôo', choices=tipos_de_classe)
    email           = forms.EmailField(label='Email', max_length=150)
    data_pesquisa   = forms.DateField(label='Data da pesquisa',
                                      disabled=True,
                                      initial=datetime.today
    )
    info_extra      = forms.CharField(label='Informações Extras',
                                      max_length=200,
                                      widget=forms.Textarea,
                                      required=False
    )

    def clean(self) :
        """ Função Clean """
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('ida')
        data_volta = self.cleaned_data.get('volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_de_erros = {}
        campo_tem_algum_numero(origem, 'origem', lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        data_de_ida_maior_que_data_volta(data_ida,data_volta, lista_de_erros)
        data_de_ida_menor_que_hoje(data_ida, data_pesquisa, lista_de_erros)
        if lista_de_erros is not None:
            for erro, mensagem_erro in lista_de_erros.items():
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data
