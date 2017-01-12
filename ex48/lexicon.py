
lexicon = {
    ('direcoes', 'norte'),
    ('direcoes', 'sul'),
    ('direcoes', 'oeste'),
    ('direcoes', 'leste')
    }

def scan(texto):

    palavras = texto.lower().split()
    pares = []

    for palavra in palavras:
        tipo_de_palavra = lexicon[palavra]
        tuplas = (palavra, tipo_de_palavra) 
        pares.append(tuplas)

    return pares