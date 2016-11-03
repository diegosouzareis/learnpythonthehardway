# coding: utf-8
from di import a, b, c, d, e, f, g, h, i, j1, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, os, qs, ps, z2, ti, u2, z3, z4, z5, z6, r2, r3, r4

def dino():
	print (i + "%s " + nome_visitante) % sala
	print j1
	print k
	print l
	primeira_escolha = raw_input()
	if primeira_escolha == "1":
		print m
	elif primeira_escolha == "2":
		escolha = raw_input(n)
		if escolha == t or escolha == ti:
			buraco_negro()
		elif escolha == u or escolha == u2:
			dino()
	elif primeira_escolha == "3":
		menu_principal()
	else:
		print v
		menu_principal()

def menu_principal():
	print s
	sala = raw_input()
	if sala == o or sala == os:
		dino()
	elif sala == q or sala == qs:
		sauna()
	elif sala == p or sala == ps:
		wow()
	else:
		print z2


def buraco_negro():
	contador = 0
	while (contador < 9):
   		print z5, contador
        contador = contador + 1
	print z6	

def sauna():
	print r
	escolha_sauna = raw_input()
	if escolha_sauna == "1":
		print z4
	elif escolha_sauna == "2":
		print z3
	else:
		menu_principal()

def wow():
	print r2
	escolha_wow = raw_input()
	if escolha_wow == "1":
		print r3
	elif escolha_wow == "2":
		print r4
	else:
		menu_principal()


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
		wow()
	elif sala == q or sala == qs:
		sauna()
	else:
		print z2

inicio()


