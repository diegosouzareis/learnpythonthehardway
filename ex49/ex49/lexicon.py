lexicon = {'norte': 'direcao', 
			'sul':'direcao', 
			'oeste': 'direcao', 
			'vai': 'verbo',
			'mata': 'verbo',
			'come': 'verbo',
			'o': 'para',
			'dentro': 'para',
			'para': 'para',
			'urso': 'noun',
			'princesa': 'noun',
			'IAS': 'error'}


def scan(texto):
        texto = texto
        palavras = texto.split()
        conteudo = []
        for palavra in palavras:
        	try:
        		categoria= 'numero'
        		valor = int(palavra)
        		conteudo.append((categoria, valor))
        	except:
        		categoria = lexicon.get(palavra, 'error')
        		valor = palavra
        		conteudo.append((categoria, palavra))
        return conteudo