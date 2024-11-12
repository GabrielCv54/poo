import json
from sqlalchemy import create_engine, Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

db = create_engine("sqlite:///guild.db", echo=True)
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Individuo(Base):
    __tablename__ = "Cidadões"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    reino = Column("reino", String)
    raça = Column("raça", String)

    def __init__(self, nome, idade, reino, raça):
        self.nome = nome
        self.idade = idade
        self.reino = reino
        self.raça = raça

    def atualizar_idade(self, nova_idade):
        self.idade = nova_idade

class Aventureiro(Individuo):
    __tablename__ = "Aventureiros"
    id = Column(Integer, ForeignKey("Cidadões.id"), primary_key=True)
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    reino = Column("reino", String)
    raça = Column("raça", String)
    rank = Column("rank", String)
    habilidades = Column("habilidades", Text)  

    individuo = relationship("Individuo", backref="aventureiros", uselist=False)

    def __init__(self, nome, idade, reino, raça, rank):
        super().__init__(nome, idade, reino, raça)
        self.rank = rank
        self.habilidades = json.dumps([])  

    def acessar_habilidades(self):
        return json.loads(self.habilidades)

    def adicionar_habilidade(self, habilidade):
        habilidades = json.loads(self.habilidades)
        habilidades.append(habilidade)
        self.habilidades = json.dumps(habilidades)

    def remover_habilidade(self, habilidade):
        habilidades = json.loads(self.habilidades)
        habilidades.remove(habilidade)
        self.habilidades = json.dumps(habilidades)

    def acessar_rank(self):
        return self.rank

    def atualizar_rank(self, rank):
        self.rank = rank

    def aventureiro_info(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade}\nReino: {self.reino}\nRaça: {self.raça}\nRank: {self.rank}\nHabilidades: {", ".join(self.acessar_habilidades())}')

rank_ordem = ["E", "D", "C", "B", "A", "S"]

def rank_valido(rank):
    return rank in rank_ordem

class Missao(Base):
    __tablename__ = "Missões"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    descricao = Column("descricao", String)
    dificuldade = Column("dificuldade", String)
    recomendado = Column("recomendado", String)
    designados = Column("designados", Text, default="[]")  

    def __init__(self, nome, descricao, dificuldade, recomendado, designados=None):
        self.nome = nome
        self.descricao = descricao
        self.dificuldade = dificuldade
        self.recomendado = recomendado
        self.designados = json.dumps(designados or [])  

    def adicionar_designado(self, designado):
        designados = json.loads(self.designados)
        designados.append(designado)
        self.designados = json.dumps(designados)
        session.commit()  

    def info_missao(self):
        designados = json.loads(self.designados)
        print(f'Missão: {self.nome}\nDescrição: {self.descricao}\nDificuldade: {self.dificuldade}\nRecomendado: {self.recomendado}\nDesignados: {", ".join(designados)}')

def carregar_habilidades_do_arquivo(arquivo_json):
    with open(arquivo_json, 'r') as file:
        habilidades = json.load(file)
    return habilidades

def criar_aventureiro(nome, idade, reino, raça, rank):
    try:
        aventureiro = Aventureiro(nome=nome, idade=idade, reino=reino, raça=raça, rank=rank)
        session.add(aventureiro)  
        session.commit()  
        print(f'Aventureiro {nome} criado com sucesso!')
    except ValueError as e:
        print(f"Erro de valor: {e}")
    except Exception as e:
        session.rollback()  
        print(f"Ocorreu um erro: {e}")


def adicionar_habilidades_ao_aventureiro(aventureiro_id, habilidades):
    aventureiro = session.query(Aventureiro).filter(Aventureiro.id == aventureiro_id).first()
    if aventureiro:
        for habilidade in habilidades:
            aventureiro.adicionar_habilidade(habilidade["nome"])
        session.commit()
        print(f'Habilidades adicionadas ao aventureiro {aventureiro.nome} com sucesso!')
    else:
        print(f'Aventureiro com ID {aventureiro_id} não encontrado.')

def atualizar_aventureiro(aventureiro_id, nome=None, idade=None, reino=None, raça=None, rank=None):
    aventureiro = session.query(Aventureiro).filter(Aventureiro.id == aventureiro_id).first()
    if aventureiro:
        if nome:
            aventureiro.nome = nome
        if idade:
            aventureiro.idade = idade
        if reino:
            aventureiro.reino = reino
        if raça:
            aventureiro.raça = raça
        if rank:
            if rank_valido(rank):
                aventureiro.rank = rank
            else:
                print(f"Rank {rank} inválido!")
                return
        session.commit()
        print(f'Aventureiro {aventureiro.nome} atualizado com sucesso!')
    else:
        print(f'Aventureiro com ID {aventureiro_id} não encontrado.')

def excluir_aventureiro(aventureiro_id):
    aventureiro = session.query(Aventureiro).filter(Aventureiro.id == aventureiro_id).first()
    if aventureiro:
        session.delete(aventureiro)
        session.commit()
        print(f'Aventureiro {aventureiro.nome} excluído com sucesso!')
    else:
        print(f'Aventureiro com ID {aventureiro_id} não encontrado.')

def criar_missao(nome, descricao, dificuldade, recomendado, designados=None):
    missao = Missao(nome=nome, descricao=descricao, dificuldade=dificuldade, recomendado=recomendado, designados=designados)
    session.add(missao)
    session.commit()
    print(f'Missão "{nome}" criada com sucesso!')

def listar_missoes():
    missoes = session.query(Missao).all()
    for missao in missoes:
        missao.info_missao()

def atualizar_missao(missao_id, nome=None, descricao=None, dificuldade=None, recomendado=None, designados=None):
    missao = session.query(Missao).filter(Missao.id == missao_id).first()
    if missao:
        if nome:
            missao.nome = nome
        if descricao:
            missao.descricao = descricao
        if dificuldade:
            missao.dificuldade = dificuldade
        if recomendado:
            missao.recomendado = recomendado
        if designados:
            missao.designados = json.dumps(designados)
        session.commit()
        print(f'Missão "{missao.nome}" atualizada com sucesso!')
    else:
        print(f'Missão com ID {missao_id} não encontrada.')

def excluir_missao(missao_id):
    missao = session.query(Missao).filter(Missao.id == missao_id).first()
    if missao:
        session.delete(missao)
        session.commit()
        print(f'Missão "{missao.nome}" excluída com sucesso!')
    else:
        print(f'Missão com ID {missao_id} não encontrada.')

def listar_aventureiros():
    aventureiros = session.query(Aventureiro).all()
    for aventureiro in aventureiros:
        aventureiro.aventureiro_info()

Base.metadata.create_all(db)

import json


#criar_aventureiro("Ares", 30, "Reino das Sombras", "Elfo", "A")
#criar_missao("Defesa do Castelo", "Proteja o castelo contra o ataque inimigo.", "Alta", "Reino das Sombras")

#criar_missao("Mate o Rei das trevas",'Matar o rei do império das Trevas','Média a Alta','Rank A','Ares')

#criar_aventureiro("Gandalf", 1000, "Reino das luz", "Mago", "S")

#habilidades=carregar_habilidades_do_arquivo('habilidades.json')


#aventureiro = session.query(Aventureiro).filter(Aventureiro.id == 1).first()

#if aventureiro:
   # aventureiro.adicionar_habilidade("Mestre da Espada")
    #aventureiro.aventureiro_info() 
#else:
 #   print("Aventureiro não encontrado.")

#missao = session.query(Missao).filter(Missao.nome == "Defesa do Castelo").first()
#if missao:
  #  missao.adicionar_designado("Ares")
 #   missao.info_missao()
#else:
   # print("Missão não encontrada.")

#missao = session.query(Missao).filter(Missao.nome == "Defesa do Castelo").first()
#if missao:
   # atualizar_missao(missao.id, nome="Defesa do Castelo - Atualizada", descricao="Proteja o castelo e recupere a torre.", dificuldade="Muito Alta")
#    missao.info_missao()
#else:
 #   print("Missão não encontrada.")

#missao = session.query(Missao).filter(Missao.nome == "Defesa do Castelo - Atualizada").first()
#if missao:
 #   excluir_missao(1)
#else:
 #   print("Missão não encontrada.")

aventureiro = session.query(Aventureiro).filter(Aventureiro.nome == "Ares").first()
if aventureiro:
     aventureiro.atualizar_rank("T")
else:
    print("Aventureiro não encontrado.")

