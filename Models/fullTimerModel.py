from sqlalchemy import Column, Integer, String, DateTime
from Models.init import Base

class FullTimer(Base):
    __tablename__ = 'FullTimers'

    idFullTimer = Column(Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
            return (f"<FullTimers(idFullTimer={self.idFullTimer}>")