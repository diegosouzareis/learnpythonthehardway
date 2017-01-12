from nose.tools import *
from ex48 import lexicon


def test_direcoes():
    assert_equal(lexicon.scan("norte"), [('direcao', 'norte')])
    resultado = lexicon.scan("norte sul oeste")
    assert_equal(resultado, [('direcao', 'norte'),
                          ('direcao', 'sul'),
                          ('direcao', 'oeste')])

def test_verbos():
    assert_equal(lexicon.scan("vai"), [('verbo', 'vai')])
    resultado = lexicon.scan("vai mata come")
    assert_equal(resultado, [('verbo', 'vai'),
                          ('verbo', 'mata'),
                          ('verbo', 'come')])


def test_para():
    assert_equal(lexicon.scan("o"), [('para', 'o')])
    resultado = lexicon.scan("o dentro para")
    assert_equal(resultado, [('para', 'o'),
                          ('para', 'dentro'),
                          ('para', 'para')])


def test_nouns():
    assert_equal(lexicon.scan("urso"), [('noun', 'urso')])
    resultado = lexicon.scan("urso princesa")
    assert_equal(resultado, [('noun', 'urso'),
                          ('noun', 'princesa')])

def test_numeros():
    assert_equal(lexicon.scan("1234"), [('numero', 1234)])
    resultado = lexicon.scan("3 91234")
    assert_equal(resultado, [('numero', 3),
                          ('numero', 91234)])


def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    resultado = lexicon.scan("urso IAS princesa")
    assert_equal(resultado, [('noun', 'urso'),
                          ('error', 'IAS'),
                          ('noun', 'princesa')])
    