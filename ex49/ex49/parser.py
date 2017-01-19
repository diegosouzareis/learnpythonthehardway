class ParserError(Exception):
    pass


class Sentenca(object):

    def __init__(self, sujeito, verbo, obj):
        self.sujeito = sujeito[1]
        self.verbo = verbo[1]
        self.objeto = obj[1]

    def to_tuple(self):
        return (self.sujeito, self.verbo, self.objeto)


def espiar(lista_de_palavras):
	if lista_de_palavras:
	    palavra = lista_de_palavras[0]
	    return palavra[0]
	else:
	    return None


def iniciar(lista_de_palavras, espera):
    if lista_de_palavras:
        palavra = lista_de_palavras.pop(0)
        if palavra[0] == espera:
            return palavra
        else:
            return None


def pular(lista_de_palavras, tipo_de_palavra):
    while espiar(lista_de_palavras) == tipo_de_palavra:
        iniciar(lista_de_palavras, tipo_de_palavra)


def parse_verbo(lista_de_palavras):
    pular(lista_de_palavras, 'stop')
    if espiar(lista_de_palavras) == 'verbo':
        return iniciar(lista_de_palavras, 'verbo')
    else:
        raise ParserError("Esperava um verbo")


def parse_objeto(lista_de_palavras):
    pular(lista_de_palavras, 'stop')
    proxima_palavra = espiar(lista_de_palavras)
    if proxima_palavra == 'noun':
        return iniciar(lista_de_palavras, 'noun')
    elif proxima_palavra == 'direcao':
        return iniciar(lista_de_palavras, 'direcao')
    else:
        raise ParserError("Esperava um substantivo ou direcao a seguir.")


def parse_sujeito(lista_de_palavras):
	pular(lista_de_palavras, 'stop')
	proxima_palavra = espiar(lista_de_palavras)
	if proxima_palavra == 'noun':
		return iniciar(lista_de_palavras, 'noun')
	elif proxima_palavra == 'verbo':
		return ('noun', 'player')
	else:
		raise ParserError("Esperava um verbo a seguir.")


def parse_sentenca(lista_de_palavras):
    sujeito = parse_sujeito(lista_de_palavras)
    verbo = parse_verbo(lista_de_palavras)
    obj = parse_objeto(lista_de_palavras)

    return Sentenca(sujeito, verbo, obj)

