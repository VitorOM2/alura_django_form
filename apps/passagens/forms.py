# pylint: disable=import-error
""" Módulo para a criação de formulários """
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe
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

    def clean(self) -> str:
        """ Verifica se o campo origem é válido """
        origem = self.cleaned_data.get('origem')
        if any(char.isdigit() for char in origem):
            raise forms.ValidationError('Origem inválida: Não inclua números')
        return origem
    