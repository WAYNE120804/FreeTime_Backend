from sqlalchemy import Column, Integer, String, DateTime, LargeBinary
from Models.init import Base

class Punishment(Base):
    __tablename__ = 'Punishments'

    idPunishment = Column(Integer, primary_key=True, autoincrement=True)
    badWorksDone = Column(LargeBinary, nullable=False)
    panicButtons = Column(LargeBinary, nullable=False)


    def __repr__(self):
        return (f"<Punishments(idPunishment={self.idPunishment}, badWorksDone={self.badWorksDone}, "
                f"panicButtons={self.panicButtons})>")