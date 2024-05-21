from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela

class Tecnico(db.Model):
    __tablename__ = "equipamento"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    equipamento  = db.Column(db.String(200))
    marca  = db.Column(db.String(200))
    quantidade = db.Column(db.Integer)
    acessorios = db.Column(db.String(200))
    observacoes = db.Column(db.String(200))
    fk_nivel_id= db.Column(db.Integer,db.ForeignKey('nivel.id'))

