from sqlalchemy import create_engine, Column, Text, Integer,BigInteger, ForeignKey, Date, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, column_property
from sqlalchemy.sql import case
from datetime import datetime

engine = create_engine('sqlite:///goodlistner.db') # my databse that will contain all the Tables belows(defined in class)
engine.connect()

Base = declarative_base()


class Listners(Base): # defining Listner table

    __tablename__ = "Listners"

    listner_id= Column(Integer,primary_key=True,unique=True)
    listner_firstName=Column(Text,nullable=False)
    listner_lastName=Column(Text,nullable=False)
    listner_email=Column(Text,nullable=False)
    listner_phoneNumber=Column(BigInteger,nullable=False)

    def __init__(self, listner_id, listner_firstName,listner_lastName, listner_email, listner_phoneNumber):
        self.listner_id = listner_id
        self.listner_firstName = listner_firstName
        self.listner_lastName = listner_lastName
        self.listner_email = listner_email
        self.listner_phoneNumber = listner_phoneNumber
   

class Talkers(Base): # defining Talkers Table

    __tablename__ = "Talkers"

    talker_id=Column(Integer,primary_key=True, unique=True)
    listner_id = Column(Integer, ForeignKey('Listners.listner_id'))
    talker_firstName=Column(String(25),nullable=False)
    talker_lastName=Column(String(25),nullable=False)
    talker_email=Column(String(80),nullable=False)
    talker_phoneNumber=Column(BigInteger,nullable=False)

    def __init__(self,talker_id, talker_firstName, talker_lastName, talker_email, talker_phoneNumber):
        self.talker_id = talker_id
        self.talker_firstName = talker_firstName
        self.talker_lastName = talker_lastName
        self.talker_email = talker_email
        self.talker_phoneNumber = talker_phoneNumber

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()