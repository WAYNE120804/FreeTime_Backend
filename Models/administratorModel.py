from sqlalchemy import Column, Integer, String, DateTime
from Models.init import Base

class Administrator(Base):
    __tablename__ = 'Administrator'

    idAdministrator = Column(Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
            return (f"<Administrator(idAdministrator={self.idAdministrator}>")