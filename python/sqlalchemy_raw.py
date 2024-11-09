from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

class Erros(Exception):
     pass


engine=create_engine("sqlite:///rpg.db ")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

#Classe Individuo
class Individuo(Base):
   __tablename__='Indíviduo'

   nome= Column(String)
   id=Column(Integer,primary_key=True,autoincrement=True)
   idade=Column (Integer)
   reino=Column(String)
   raça=Column(String)

def __init__(self,nome,id,idade,reino,raça):
        self.nome = nome
        self.id = id
        self.idade = idade
        self.reino = reino
        self.raça = raça

def atualizar_idade(nova_idade):
    return  nova_idade

def __repr__(self):
      return f'Nome:{self.nome},Id:{self.id},Reino:{self},Raça:{self.raça}'
    

#Classe Aventureiro
class Aventureiro(Base):
     __tablename__='Aventureiro'

     nome= Column(String)
     id_aventureiro=Column(Integer,primary_key=True,autoincrement=True)
     idade=Column(Integer)
     reino=Column(String)
     habilidades=Column(String)
     rank=Column(String,ForeignKey('Indivíduo.id_individuo'))
     individuo=relationship('Individuo',backref='Aventureiro')


def __init__(self,id_aventureiro, nome, idade, reino, raça, rank,habilidades):
        self.nome = nome
        self.idade = idade
        self.reino = reino
        self.raça = raça
        self.id_aventureiro = id_aventureiro
        self.habilidades = habilidades
        self.rank = rank

def acessar_habilidades(self):
   return self.habilidades

def adicionar_habilidade(self,habilidade):
   self.habilidades.append(habilidade)
 
def remover_habilidade(self,habilidade):
   self.habilidades.remove(habilidade)
   
def acessar_rank(self):
      return self.rank   

def atualizar_rank(self,ranking):
   self.rank = ranking

def __repr__(self):
        return f'Aventureiro: {self.nome}|Código:{self.id}|Idade: {self.idade}|Reino: {self.reino}|Raça: {self.raça}|Habilidades: {self.habilidades}|Rank: {self.rank}'

# Classe Missão
class Missão(Base):
  __tablename__='Missão'

  id_missao=Column(Integer,primary_key=True)
  nome_missao=Column(String)
  descricao=Column(String)
  dificuldade=Column(String)
  recomendado=Column(String)
  designados=relationship('Aventureiro  ',backref='Missão')

def __init__(self,id_missao ,nome, descricao, dificuldade, recomendado):
        self.nome = nome
        self.id_missao = id_missao
        self.descricao = descricao
        self.dificuldade = dificuldade
        self.recomendado = recomendado
        self.designados = []

def adicionar_designados(self,designado):
   self.designados.append(designado)

def __repr__(self):
     return f"Missão designada a : {self.designados}"

#Criação de tabelas e do banco de dados
Base.metadata.create_all(engine)

#Insert
jaun=Individuo(nome='Jaun',id=1,idade=21,reino='Avalor',raça='Humano')
session.add(jaun)
session.commit()

#SELECT
individuo=session.query(Individuo).all()
print(individuo)


session.close()

