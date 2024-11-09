from infra.configurações.connection import DBConnectionHandler
from infra.Entidades.Individuo import Individuo

class IndividuoRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Individuo).all()
            return data
        
    def insert(self,nome,id,idade,reino,raça):
        with DBConnectionHandler as db:
            insert=Individuo(nome=nome,id=id,idade=idade,reino=reino,raça=raça)
            db.session.add(insert)
            db.session.commit()
    
    def delete(self,nome):
        with DBConnectionHandler as db:
            db.session.query(Individuo).filter(Individuo.nome == nome).delete()
            db.session.commit()
        
    def update(self,nome,id,idade):
        with DBConnectionHandler as db:
            db.session.query(Individuo).filter(Individuo.nome == nome).update({'idade':idade})
            db.session.commit()