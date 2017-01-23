class Quarto(objeto):
	def __init__(self, nome, descricao):
		self.nome = nome
		self.descricao = descricao
		self.paths = {}

	def ir(self, direcao):
		return self.paths.get(direcao, None)
		
	def adiciona_paths(self, paths):
		self.paths.update(paths)
		
		
corredor_central = Quarto("Corredor Central",
"""
Os Gothons do planeta Percal # 25 invadiram sua nave e destruíram
Sua tripulação inteira. Você é o último membro sobrevivente e seu último
Missão é obter a bomba de destruição de nêutrons do Arsenal de Armas,
Colocá-lo na ponte, e explodir o navio depois de entrar em um
Escape pod.
Você está correndo pelo corredor central até o Arsenal de Armas quando
Um Gothon salta para fora, pele vermelha escamosa, dentes sujos e sujos e traje de palhaço mal
Fluindo em torno de seu corpo cheio de ódio. Ele está bloqueando a porta para o
Armory e prestes a puxar uma arma para explodir você.
""")


arma_laser_armamento = Quarto("Arma Laser Armamento",
"""
Sorte para você eles fizeram você aprender insultos Gothon na academia.
Você conta a uma piada de Gothon que você conhece:
Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, pele fvgf nebhaq gur ubhfr.
O Gothon pára, tenta não rir, então destrói rir e não pode se mover.
Enquanto ele está rindo você corre para cima e atirá-lo quadrado na cabeça
Colocando-o para baixo, em seguida, saltar através da porta Armory Arma.
Você faz um rolo de mergulho no Armory Weapon, agachar e digitalizar o quarto
Para mais Gothons que pudessem se esconder. Está calado, calmo demais.
Você se levanta e corre para o outro lado da sala e encontra o
Bomba de nêutrons em seu recipiente. Há um bloqueio do teclado na caixa
E você precisa do código para tirar a bomba. Se você receber o código
Errado 10 vezes, em seguida, o bloqueio fecha para sempre e você não pode
Pegue a bomba O código é de 3 dígitos.
""")


a_ponte = Quarto("A Ponte",
"""
Os contêineres se abrem e o selo se quebra, deixando sair o gás.
Você pega a bomba de nêutrons e corre o mais rápido que
Ponte onde você deve colocá-lo no lugar certo.
Você explodiu na Ponte com a bomba de destruição do netron
Sob seu braço e surpreenda 5 Gothons que estão tentando
Tomar o controle do navio. Cada um deles tem um uglier ainda mais
Traje de palhaço do que o último. Eles não
Armas para fora ainda, como eles vêem a bomba ativa sob o seu
Braço e não querem ajustá-lo fora.
""")


pod_escapatorio = Quarto("Pod Escapatorio",
"""
Você aponta seu blaster para a bomba embaixo do seu braço
E os Gothons levantam as mãos e começam a suar.
Você polegada para trás para a porta, abra-a e, em seguida, cuidadosamente
Coloque a bomba no chão, apontando seu blaster para ele.
Você pula de volta pela porta, aperte o botão de fechar
E explodir a fechadura para que os Gothons não podem sair.
Agora que a bomba é colocada você corre para o pod de fuga para
Saia dessa lata de lata.
Você corre através do navio tentando desesperadamente
A vara de escape antes que o navio inteiro explode. Parece que
Praticamente nenhum Gothons está no navio, então sua corrida está
interferência. Você chega à câmara com as vagens de
Agora precisa escolher um para tomar. Alguns deles podem ser danificados
Mas você não tem tempo para olhar. Há 5 pods, um deles
você pega?
""")


o_vencedor_final = Quarto("O Final",
"""
Você pula no pod 2 e aperta o botão de ejeção.
O pod desliza facilmente para o espaço para
O planeta abaixo. Como ele voa para o planeta, você olha
E ver o seu navio implodir e explodir como um
Estrela brilhante, tirando o navio Gothon ao mesmo
Tempo. Você ganhou!
""")


o_perdedor_final = Quarto("O Final",
"""
Você pula em um pod aleatório e aperta o botão de ejeção.
O pod escapa para fora no vazio do espaço, então
Implode quando o casco rompe, esmagando seu corpo
Em geléia de geléia.
"""
)

pod_escapatorio.add_paths({
    '2': o_vencedor_final,
    '*': o_perdedor_final
})

morte_generica = Quarto("morte", "Voce morreu.")

a_ponte.adiciona_paths({
    'jogue a bomba': morte_generica,
    'lentamente a bomba': pod_escapatorio
})

arma_laser_armamento.adiciona_paths({
    '0132': a_ponte,
    '*': morte_generica
})

corredor_central.add_paths({
    'atire!': morte_generica,
    'dodge!': morte_generica,
    'conte uma piada': arma_laser_armamento
})

START =  corredor_central