# coding: utf-8
from di import a, b, c, d, e, f, g, h, i, j1, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, os, qs, ps, z2, ti, u2

def dino():
	print (i + "%s " + nome_visitante) % sala
	print j1
	print k
	print l
	primeira_escolha = raw_input()
	if primeira_escolha == "1":
		print "gravar"
	elif primeira_escolha == "2":
		escolha = raw_input("Deseja mesmo entrar?")
		if escolha == t or escolha == ti:
			buraco_negro()
		elif escolha == u or escolha == u2:
			dino()
	elif primeira_escolha == "3":
		print "23"
	else:
		print "32"

def buraco_negro():
	contador = 0
	while (contador < 9):
   		print 'VOCÊ NAO DEVERIA TER FEITO ISOOOOO, ESTAVA BRINCANDOOOOOOOOOOO, AGORA O NUBANK ESTA EM PARADO NO TEMPOOOOO', contador
        contador = contador + 1
	print "DEU MUITO RUIMMMMM"	

def sauna():
	print "oi"

def wow():
	print "oi2"

def inicio():
	print a
	print b
	global nome_visitante
	nome_visitante = raw_input("%s " % c)
	print d
	print f
	print g
	print h

	global sala
	sala = raw_input()

	if sala == o or sala == os:
		dino()
	elif sala == p or sala == ps:
		sauna()
	elif sala == q or sala == qs:
		wow()
	else:
		print z2

inicio()