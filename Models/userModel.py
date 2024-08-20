from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    idUser = Column(Integer, primary_key=True, autoincrement=True)
    fullName = Column(String, nullable=False)
    identification = Column(String, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    phoneNumber = Column(String, nullable=True)
    country = Column(String, nullable=False)
    city = Column(String, nullable=False)
    address = Column(String, nullable=True)
    freeTimer = Column(Boolean, default=False)
    fullTimer = Column(Boolean, default=False)
    password = Column(String, nullable=False)
    balance = Column(Integer, default=0)

    def __repr__(self):
        return (f"<User(idSupport={self.idUser}, fullName='{self.fullName}', email='{self.email}'>")
