from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Compte(Base):
    __tablename__ = 'compte'
    id = Column(Integer, primary_key=True)
    Nom = Column(String)
    Description = Column(String)

    def __repr__(self):
        return "<Compte(Nom='{}', Description='{}')>" \
            .format(self.Nom, self.Description)


class Bucket(Base):
    __tablename__ = 'bucket'
    id = Column(Integer, primary_key=True)
    Nom = Column(String)
    Taille = Column(String)
    Type = Column(String)
    compteId = Column(Integer, ForeignKey('compte.id'))

    def __repr__(self):
        return "<Bucket(Nom='{}', Taille='{}', Type={}, compteId='{}')>" \
            .format(self.Nom, self.Taille, self.Type, self.compteId)