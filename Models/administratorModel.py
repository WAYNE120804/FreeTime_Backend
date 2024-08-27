from sqlalchemy import Column, Integer, String, DateTime
from Models.init import Base

class Administrator(Base):
    __tablename__ = 'Administrators'

    idAdministrator = Column(Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
            return (f"<Administrators(idAdministrator={self.idAdministrator}>")