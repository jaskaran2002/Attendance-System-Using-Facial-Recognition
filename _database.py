from click import echo
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'students'
    roll_no = Column('id', Integer, primary_key=True)
    name = Column('id', String)
    
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

    def __repr__(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}")

engine = create_engine('sqlite:///users.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()


session.close()
