from infra.configurações.importações import Base
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

#Classe Aventureiro
class Aventureiro(Base):
     __tablename__='Aventureiro'

     nome= Column(String)
     id_aventureiro=Column(Integer,primary_key=True,autoincrement=True)
     idade=Column(Integer)
     reino=Column(String)
     habilidades=Column(String)
     rank=Column(String,ForeignKey('Indivíduo.id'))
     individuo=relationship('Individuo',backref='Aventureiro')

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
        return f'Aventureiro: { self.nome}|Código:{self.id}|Idade: {self.idade}|Reino: {self.reino}|Raça: {self.raça}|Habilidades: {self.habilidades},|Rank: {self.rank}'