class Individuo:
    def __init__(self,nome,idade,reino,raça):
        self.nome = nome
        self.idade = idade
        self.reino = reino
        self.raça = raça

    def atualizar_idade(self,nova_idade):
        self.idade = nova_idade

class Aventureiro(Individuo):
    def __init__(self, nome, idade, reino, raça, rank):
        super().__init__(nome, idade, reino, raça)
        self.__habilidades = []
        self.__rank = rank

    def acessar_habilidades(self):
        return self.__habilidades

    def adicionar_habilidade(self,habilidade):
        self.__habilidades.append(habilidade)

    def remover_habilidade(self,habilidade):
        self.__habilidades.remove(habilidade)

    def acessar_rank(self):
        return self.__rank

    def atualizar_rank(self,ranking):
        self.__rank = ranking

    def aventureiro_info(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade}\nReino: {self.reino}\nRaça: {self.raça}\nHabilidades: {self.acessar_habilidades()}\nRank: {self.acessar_rank()}')

class Missao:
    def __init__(self, nome, descricao, dificuldade, recomendado, designados):
        self.nome = nome
        self.descricao = descricao
        self.dificuldade = dificuldade
        self.recomendado = recomendado
        self.designados = []

    def adicionar_designados(self, designado):
        self.designados.append(designado)

    def info_missao(self):
        print(f'Essa missão foi designada ao {self.designados}')




# Criando Indivíduos
individuo1 = Individuo(nome="Liora", idade=28, reino="Aeloria", raça="Humana")
individuo2 = Individuo(nome="Thalor", idade=35, reino="Druun", raça="Elfo")

# Atualizando Idades dos Indivíduos
individuo1.atualizar_idade(29)
individuo2.atualizar_idade(36)


# Criando Aventureiros
aventureiro1 = Aventureiro(nome="Korin", idade=24, reino="Vardor", raça="Anão", rank="D")
aventureiro2 = Aventureiro(nome="Seraphine", idade=22, reino="Veldor", raça="Humana", rank="C")
aventureiro3 = Aventureiro(nome="Thalor", idade=30, reino="Druun", raça="Elfo", rank="B")

# Adicionando Habilidades aos Aventureiros
aventureiro1.adicionar_habilidade("Machado de Guerra")
aventureiro1.adicionar_habilidade("Força Bruta")
aventureiro2.adicionar_habilidade("Flechas de Longo Alcance")
aventureiro2.adicionar_habilidade("Magia Elemental")
aventureiro3.adicionar_habilidade("Magia de Fogo")
aventureiro3.adicionar_habilidade("Espada Longa")

# Exibindo Informações dos Aventureiros
aventureiro1.aventureiro_info()
aventureiro2.aventureiro_info()
aventureiro3.aventureiro_info()

# Criando Missões
missao1 = Missao(nome="Resgate na Fortaleza", descricao="Resgatar o príncipe de Veldor", dificuldade="Alta", recomendado="C ou superior", designados=[])
missao2 = Missao(nome="Exploração de Ruínas", descricao="Explorar as ruínas antigas de Aeloria", dificuldade="Média", recomendado="D ou superior", designados=[])
missao3 = Missao(nome="Ameaça das Sombras", descricao="Lutar contra a ameaça das criaturas sombrias", dificuldade="Muito Alta", recomendado="B ou superior", designados=[])
missao4 = Missao(nome="Caçada ao Dragão", descricao="Caçar o dragão vermelho nas montanhas", dificuldade="Extrema", recomendado="B ou superior", designados=[])

# Adicionando Aventureiros às Missões
missao1.adicionar_designados(aventureiro2.nome)  
missao2.adicionar_designados(aventureiro1.nome)  
missao2.adicionar_designados(aventureiro2.nome)  
missao3.adicionar_designados(aventureiro3.nome)  
missao4.adicionar_designados(aventureiro3.nome)  

# Exibindo informações das missões
missao1.info_missao()
missao2.info_missao()
missao3.info_missao()
missao4.info_missao()

