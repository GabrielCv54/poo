from infra.configurações.importações import Base
from sqlalchemy import  Column, Integer, String, ForeignKey

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