from django import forms


class PassagemForms(forms.Form):
    """ Cria o formulário de passagens """
    origem  = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    ida     = forms.DateField(label='Ida')
    volta   = forms.DateField(label='Volta')
    