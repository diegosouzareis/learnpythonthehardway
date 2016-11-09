# coding: utf-8
from di import decisoes, salas, sim, nao, dialogos_basicos, dialogos

def dino():
	print (dialogos_basicos['6'] + "%s " + nome_visitante) % sala
	print dialogos['3']
	print dialogos['4']
	print decisoes['terceira']
	primeira_escolha = raw_input()
	if primeira_escolha == "1":
		print dialogos['1']
	elif primeira_escolha == "2":
		escolha = raw_input(dialogos['2'])
		if escolha == sim or escolha == sim.lower().strip():
			buraco_negro()
		elif escolha == nao or escolha == nao.lower().strip():
			dino()
	elif primeira_escolha == "3":
		menu_principal()
	else:
		print dialogos['6']
		menu_principal()

def menu_principal():
	print dialogos_basicos['8']
	sala = raw_input()
	if sala == salas['sala1'] or sala == salas['sala1'].lower().strip():
		dino()
	elif sala == salas['sala2'] or sala == salas['sala2'].lower().strip():
		sauna()
	elif sala == salas['sala3'] or sala == salas['sala3'].lower().strip():
		wow()
	else:
		print dialogos['7']


def buraco_negro():
	contador = 0
	while (contador < 9):
   		print dialogos['10'], contador
        contador = contador + 1
	print dialogos['11']	

def sauna():
	print decisoes['quarta']
	escolha_sauna = raw_input()
	if escolha_sauna == "1":
		print dialogos['9']
	elif escolha_sauna == "2":
		print dialogos['8']
	else:
		menu_principal()

def wow():
	print decisoes['segunda']
	escolha_wow = raw_input()
	if escolha_wow == "1":
		print dialogos['12']
	elif escolha_wow == "2":
		print dialogos['13']
	else:
		menu_principal()

def inicio():
	print dialogos_basicos['4']
	print dialogos_basicos['3']
	global nome_visitante
	nome_visitante = raw_input("%s " % dialogos_basicos['2'])
	print dialogos_basicos['1']
	print dialogos_basicos['5']
	print dialogos_basicos['9']
	print decisoes['primeira']

	global sala
	sala = raw_input()

	if sala == salas['sala1'] or sala == salas['sala1'].lower().strip():
		dino()
	elif sala == salas['sala2'] or sala == salas['sala2'].lower().strip():
		sauna()
	elif sala == salas['sala3'] or sala == salas['sala3'].lower().strip():
		wow()
	else:
		print dialogos['7']

inicio()
