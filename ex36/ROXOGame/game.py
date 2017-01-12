# coding: utf-8
from di import decisoes, salas, sim, nao, dialogos_basicos, dialogos

def dino(estado):
	print dialogos["dino"]["bem_vindo"] + estado["nome_visitante"] + estado["sala"]
	print dialogos["dino"]["oque_fazemos"]
	print dialogos["dino"]["oque_temos"]
	print dialogos["dino"]["decisao"]
	primeira_escolha = read_lower()
	if primeira_escolha == "1":
		print dialogos["dino"]["ops"]
	elif primeira_escolha == "2":
		escolha = read_lower(dialogos['2'])
		if escolha == sim:
			buraco_negro()
		elif escolha == nao:
			dino()
	elif primeira_escolha == "3":
		menu_principal(estado)
	else:
		print dialogos["dino"]["deselegante"]
		menu_principal(estado)

def menu_principal(estado):
	print dialogos["menu_principal"]["escolha_sala"]
	estado["sala"] = read_lower()
	if estado["sala"] == salas['sala1']:
		dino(estado)
	elif estado["sala"] == salas['sala2']:
		sauna()
	elif estado["sala"] == salas['sala3']:
		wow()
	else:
		print dialogos["menu_principal"]["erro"]

def buraco_negro():
	contador = 0
	while (contador < 9):
   		print dialogos["buraco_negro"]["meu_deus"], contador
        contador = contador + 1
	print dialogos["buraco_negro"]["deu_ruim"]	

def sauna():
	print dialogos["sauna"]["decisao"]
	escolha_sauna = read_lower()
	if escolha_sauna == "1":
		print dialogos["sauna"]["tv"]
	elif escolha_sauna == "2":
		print dialogos["sauna"]["trocar_canetas"]
	else:
		menu_principal()

def wow():
	print dialogos["wow"]["decisao"]
	escolha_wow = read_lower()
	if escolha_wow == "1":
		print dialogos["wow"]["oque_procura"]
	elif escolha_wow == "2":
		print dialogos["wow"]["foto"]
	else:
		menu_principal()

def read_lower(text=""):	
	return raw_input(text).lower().strip()

def inicio(estado):
	print dialogos["inicio"]["saudacao"]
	print dialogos["inicio"]["digite_nome"]
	estado["nome_visitante"] = read_lower(dialogos_basicos['2'] + " ")
	print dialogos["inicio"]["bem_vindo"]
	print dialogos["inicio"]["explorar"]
	print dialogos["inicio"]["vamos_la"]
	print dialogos["inicio"]["decisao"]

	estado["sala"] = read_lower()

	if estado["sala"] == salas['sala1']:
		dino(estado)
	elif estado["sala"] == salas['sala2']:
		sauna()
	elif estado["sala"] == salas['sala3']:
		wow()
	else:
		print dialogos["inicio"]["erro"]
estado = {}
inicio(estado)
