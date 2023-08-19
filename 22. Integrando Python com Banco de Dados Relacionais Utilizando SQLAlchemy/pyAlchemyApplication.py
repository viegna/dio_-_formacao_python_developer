import sqlalchemy

from sqlalchemy import Integer, create_engine
from sqlalchemy import String
from sqlalchemy import Column 
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    #atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    
    address = relationship(
        #determina uma ação para n ter inconsistencia, em cascata, deletará o orfão tbm
        "Adress", back_populates="user", cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"User(id={self.id},name={self.name},fullname={self.fullname})"
    
class Adress(Base):
    __tablename__ = "adress"
    #atributos
    id = Column(Integer, primary_key=True)
    email_adress = Column(String(30), nullable=False, )
    user_id =Column(Integer,ForeignKey("user_account.id"), nullable=False)
    
    user = relationship("User", back_populates="adress")

    def __repr__(self):
        return f"Adress(id={self.id},email={self.email_adress})"
    
print(Adress.__tablename__)
print(User.__tablename__)

#conexão com banco de dados
engine = create_engine("sqlite://")

#criando classes como tabelas no bd
Base.metadata.create_all(engine)