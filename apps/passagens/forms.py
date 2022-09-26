from django import forms
from tempus_dominus.widgets import DatePicker


class PassagemForms(forms.Form):
    """ Cria o formulário de passagens """
    origem  = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    ida     = forms.DateField(label='Ida', widget=DatePicker())
    volta   = forms.DateField(label='Volta', widget=DatePicker())
    