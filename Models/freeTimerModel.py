from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Models.init import Base

class FreeTimer(Base):
    __tablename__ = 'FreeTimers'

    idFreeTimer = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String(255), nullable=False)
    #review_id = Column(Integer, ForeignKey('Reviews.id'))
    idReward = Column(Integer, ForeignKey('Rewards.idReward'))
    healthInsurance = Column(String(255), nullable=False)  # Asumiendo que PDF se almacena como una cadena de texto
    idTask = Column(Integer, ForeignKey('Tasks.idTask'))
    idPunishment = Column(Integer, ForeignKey('Punishments.idPunishment'))


   #review = relationship("Reviews", back_populates="freetimer")
    #reward = relationship("Rewards", back_populates="freetimer")
    #tasks = relationship("Tasks", back_populates="freetimer")
    #punishments = relationship("Punishments", back_populates="freetimer")

    def __repr__(self):
        return (f"<FreeTimers(id={self.idFreeTimer}, category={self.category}, "
                f"idReward={self.idReward}, healthInsurance={self.healthInsurance}, "
                f"idTask={self.idTask}, idPunishment={self.idPunishment})>")