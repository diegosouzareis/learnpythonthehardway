from nose.tools import *
from ex49 import lexicon
from ex49 import parser

def test_sentenca_obj():
    s = parser.Sentenca(('noun', 'urso'), ('verbo', 'come'), ('noun', 'porta'))
    assert_equal(s.sujeito, 'urso')
    assert_equal(s.verbo, 'come')
    assert_equal(s.objeto, 'porta')
    assert_equal(s.to_tuple(), ('urso', 'come', 'porta'))

def test_olhadinha():
    lista_de_palavras = lexicon.scan('princesa')
    assert_equal(parser.olhadinha(lista_de_palavras), 'noun')
    assert_equal(parser.olhadinha(None), None)

def test_partida():
    lista_de_palavras = lexicon.scan('princesa')
    assert_equal(parser.partida(lista_de_palavras, 'noun'), ('noun', 'princesa'))
    assert_equal(parser.partida(lista_de_palavras, 'para'), None)
    assert_equal(parser.partida(None, 'noun'), None)

def test_pular():
    lista_de_palavras = lexicon.scan('urso come porta')
    assert_equal(lista_de_palavras, [('noun', 'urso'), ('verbo', 'come'), ('error', 'porta')])
    parser.pular(lista_de_palavras, 'noun')
    assert_equal(lista_de_palavras, [('verbo', 'come'), ('error', 'porta')])

def test_parse_verbo():
    lista_de_palavras = lexicon.scan('urso come porta')
    assert_equal(parser.parse_verbo(lista_de_palavras), ('verbo', 'come'))
    word_list = lexicon.scan('urso come porta')
    assert_raises(parser.ParserError, parser.parse_verbo, lista_de_palavras)
