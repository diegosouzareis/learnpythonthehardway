# coding: utf-8
from di import decisoes, salas, sim, nao, dialogos_basicos, dialogos

def dino(estado):
	print dialogos_basicos['6'] + estado["nome_visitante"] + estado["sala"]
	print dialogos['3']
	print dialogos['4']
	print decisoes['terceira']
	primeira_escolha = read_lower()
	if primeira_escolha == "1":
		print dialogos['1']
	elif primeira_escolha == "2":
		escolha = read_lower(dialogos['2'])
		if escolha == sim:
			buraco_negro()
		elif escolha == nao:
			dino()
	elif primeira_escolha == "3":
		menu_principal()
	else:
		print dialogos['6']
		menu_principal()

def menu_principal(estado):
	print dialogos_basicos['8']
	estado["sala"] = read_lower()
	if estado["sala"] == salas['sala1']:
		dino()
	elif estado["sala"] == salas['sala2']:
		sauna()
	elif estado["sala"] == salas['sala3']:
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
	escolha_sauna = read_lower()
	if escolha_sauna == "1":
		print dialogos['9']
	elif escolha_sauna == "2":
		print dialogos['8']
	else:
		menu_principal()

def wow():
	print decisoes['segunda']
	escolha_wow = read_lower()
	if escolha_wow == "1":
		print dialogos['12']
	elif escolha_wow == "2":
		print dialogos['13']
	else:
		menu_principal()

def read_lower(text=""):	
	return raw_input(text).lower().strip()

def inicio(estado):
	print dialogos_basicos['4']
	print dialogos_basicos['3']
	estado["nome_visitante"] = read_lower(dialogos_basicos['2'] + " ")
	print dialogos_basicos['1']
	print dialogos_basicos['5']
	print dialogos_basicos['9']
	print decisoes['primeira']

	estado["sala"] = read_lower()

	if estado["sala"] == salas['sala1']:
		dino(estado)
	elif estado["sala"] == salas['sala2']:
		sauna()
	elif estado["sala"] == salas['sala3']:
		wow()
	else:
		print dialogos['7']
estado = {}
inicio(estado)
