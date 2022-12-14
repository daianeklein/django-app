def origem_destino_iguais(origem, destino, lista_erros):
    '''Verifica se origem e destino são iguais'''
    if origem == destino:
        lista_erros['destino'] = 'Origem e destino não podem ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_erros):
    '''Verifica se tem algum digito numerico'''
    if any(char.isdigit() for char in valor_campo):
        lista_erros[nome_campo] = 'Não inclua números neste campo'

def data_ida_maior_que_data_volta(data_ida, data_volta, lista_erros):
    '''Verifica se data de ida é maior que data de volta'''
    if data_ida > data_volta:
        lista_erros['data_volta'] = 'Data de ida não pode ser maior do que data de volta'

def data_ida_menor_data_hoje(data_ida, data_pesquisa, lista_erros):
    '''Verifica se data de ida é menor que data de hoje'''
    if data_ida < data_pesquisa:
        lista_erros['data_ida'] = 'Data de ida não pode ser menor que data de hoje'