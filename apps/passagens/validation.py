""" Módulo para as validaçãos dos campos """

def origem_destino_iguais(origem, destino, lista_de_erros):
    """ Verifica se os campos são iguais """
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser iguais'
        
def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """ Verifica se existe algum número nos campos """
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números neste campo'

def data_de_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros):
    """ Verifica se a data de ida é maior do que a de volta """
    if data_ida > data_volta:
        lista_de_erros['volta'] = 'Data de ida não pode ser maior do que data de volta'
        
def data_de_ida_menor_que_hoje(data_ida, data_pesquisa, lista_de_erros):
    """ Verifica se a data de pesquisa é menor que hoje """
    if data_ida < data_pesquisa:
        lista_de_erros['ida'] = 'Data de ida não pode ser menor que hoje'
