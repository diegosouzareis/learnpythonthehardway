# coding: utf-8
# dialogos

decisoes = {}

salas = {'sala1': 'dino',
 		 'sala2': 'sauna',
 		 'sala3': 'wow'}

sim = "sim"
nao = "nao"

dialogos = {

"inicio": {"saudacao": "Ola! tudo bem?",
		   "digite_nome": "Para começarmos digite o seu nome",
		   "bem_vindo": "Bem vindo ao ROXObank",
		   "explorar": "Hoje você poderar explorar algumas salas de reunião da aqui do ROXObank",
		   "vamos_la": "Vamos lá",
		   "decisao": """Em qual sala você quer entrar?
						 1 - Dino
						 2 - WOW
						 3 - Sauna""",
		   "erro": "Essa sala não existe ou não esta disponivel para acesso!"},

"buraco_negro": {"meu_deus": "VOCÊ NAO DEVERIA TER FEITO ISOOOOO, ESTAVA BRINCANDOOOOOOOOOOO, AGORA O ROXOBank ESTA EM PARADO NO TEMPOOOOO",
				 "deu_ruim": "DEU MUITO RUIMMMMM"},

"menu_principal": {"escolha_sala": "Escolha uma sala para entrar",
				   "erro": "Essa sala não existe ou não esta disponivel para acesso!"},

"dino": {"bem_vindo": "Bem vindo a sala ",
		 "oque_fazemos": "Aqui nesta sala costumamos fazer alguns treinamentos e videos para o Youtube",
		 "oque_temos": "Aqui tambem temos um buraco negro",
		 "decisao": """1 - Gravar um video
					   2 - entrar no buraco negro
					   3 - Sair""",
		 "ops": "Opsss hahaha, estamos sem ninguem para gravar você hoje",
		 "deselegante": "Poxa cara nao seja deselegante"},

"sauna": {"decisao": """Aqui é uma sala de reunião bem legal e bem grande tambem hahaha:
						1 - Procurar alguma coisa
						2 - Tirar foto
						3 - Sair""",
		  "tv": "Você ligou a TV, parece estar passando The Walking Dead",
		  "trocar_canetas": "Parece que precisamos trocar as canetas depois voce escreve ;)"},

"wow": {"decisao": """Aqui é uma sala de reunião bem comum, aqui voce pode:
					  1 - Ligar a TV
				      2 - Escrever no quadro
					  3 - Sair""",
		"oque_procura": "O que voce esta fazendo, cuidado com o que procura MUHAAHAHA"
		"foto": "BOAAA, depois compatilhe essa foto :)"}

}


