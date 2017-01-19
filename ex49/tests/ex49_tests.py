from nose.tools import *
from ex49 import lexicon
from ex49 import parser

def test_sentenca_obj():
    s = parser.Sentenca(('noun', 'urso'), ('verbo', 'come'), ('noun', 'porta'))
    assert_equal(s.sujeito, 'urso')
    assert_equal(s.verbo, 'come')
    assert_equal(s.objeto, 'porta')
    assert_equal(s.to_tuple(), ('urso', 'come', 'porta'))


def test_espiar():
    lista_de_palavras = lexicon.scan('princesa')
    assert_equal(parser.espiar(lista_de_palavras), 'noun')
    assert_equal(parser.espiar(None), None)


def test_iniciar():
    lista_de_palavras = lexicon.scan('princesa')
    assert_equal(parser.iniciar(lista_de_palavras, 'noun'), ('noun', 'princesa'))
    assert_equal(parser.iniciar(lista_de_palavras, 'para'), None)
    assert_equal(parser.iniciar(None, 'noun'), None)


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


def test_parse_objeto():
    lista_de_palavras = lexicon.scan('o porta')
    assert_equal(parser.parse_objeto(lista_de_palavras), ('noun', 'porta'))
    lista_de_palavras = lexicon.scan('o oeste')
    assert_equal(parser.parse_objeto(lista_de_palavras), ('direcao', 'oeste'))
    lista_de_palavras = lexicon.scan('o e')
    assert_raises(parser.ParserError, parser.parse_objeto, lista_de_palavras)


def test_parse_sujeito():
    lista_de_palavras = lexicon.scan('o urso come porta')
    s = parser.parse_sujeito(lista_de_palavras)
    assert_equal(s.to_tuple(), ('urso', 'come', 'porta'))
    lista_de_palavras = lexicon.scan('dentro come porta')
    s = parser.parse_sentenca(lista_de_palavras)
    assert_equal(s.to_tuple(), ('player', 'come', 'porta'))
    lista_de_palavras = lexicon.scan('norte come porta')
    assert_raises(parser.ParserError, parser.parse_sentenca, lista_de_palavras)


def test_parse_sentenca():
    lista_de_palavras = lexicon.scan('come porta')
    s = parser.parse_sentenca(lista_de_palavras)
    assert_equal(s.to_tuple(), ('urso', 'norte', 'porta'))


