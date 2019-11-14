from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, Compte, Bucket
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

#Create Compte
compte = Compte(
    Nom="Super Client",
    Description="Trop bien ce client"
)
session.add(compte)
session.commit()


#Read Compte
comptes = session.query(Compte)
for compte in comptes:
    print(compte.Nom)
    
# Update
compte.Nom = "Nouveau nom"
session.commit()

# Delete Compte
#session.delete(compte)
#session.commit()

#Create Bucket
bucket = Bucket(
    Nom="Super Bucket",
    Taille="Trop grand",
    Type="En plastique",
    compteId=4
)
session.add(bucket)
session.commit()


#Read Bucket
buckets = session.query(Bucket)
for bucket in buckets:
    print(bucket.Nom)
# Update
bucket.Nom = "Nouveau nom"
bucket.Taille ="Trop petit",
bucket.Type="En fer",
bucket.compteId=4
session.commit()

# Delete Bucket
session.delete(bucket)
session.commit()
