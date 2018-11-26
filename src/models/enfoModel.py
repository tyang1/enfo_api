from sqlalchemy import create_engine  
from sqlalchemy import Column, String, Integer 
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from marshmallow import fields, Schema
from flask_sqlalchemy import SQLAlchemy
from . import db

# initialize our db
# db = SQLAlchemy()
#To connect to psql, try psql -U <username> <databaseName>

# db_string = 'postgres://enfo:enfo@localhost/enfo_db'

# db = create_engine(db_string)  
# base = declarative_base()

#Why using declarative_base here:
#Instead of defining our Film class as a Table, we create a normal Python object which subclasses base and which defines __tablename__. 
class Animal(db.Model):  
    __tablename__ = 'enfo_animal2'

    name = db.Column(db.String, primary_key=True)
    wiki = db.Column(db.String)
    status = db.Column(db.String)
    img = db.Column(db.String)
    blurb = db.Column(db.String)
    scientificName = db.Column(db.String)
    
    def __init__ (self, name, wiki, status, img, blurb, scientificName):
        self.name = name
        self.wiki = wiki
        self.status = status
        self.img = img
        self.blurb = blurb
        self.scientificName = scientificName

# base.metadata.create_all(db)

class AnimalSchema (Schema):
    name = fields.Str(dump_only=True)
    wiki = fields.Str(dump_only=True)
    status = fields.Str(dump_only=True)
    img = fields.Str(dump_only=True)
    blurb = fields.Str(dump_only=True)
    scientificName = fields.Str(dump_only=True)


# Session = sessionmaker(db)  
# session = Session()




# # # Create 
# african_elephant = Animal(name="African Bush Elephant", status='UV', img='/bushelephant.jpg', blurb='The African bush elephant (Loxodonta africana), also known as the African savanna elephant, is the larger of the two species of African elephants, and the largest living terrestrial animal. These elephants were previously regarded as the same species, but the African forest elephant has been reclassified as L. cyclotis.',wiki="https://en.wikipedia.org/wiki/African_elephant", scientificName="Loxodonta africana")
# session.add(african_elephant)
# session.commit()

# Read

