from sqlalchemy import Column, Integer, String, DateTime
from Models.init import Base

class Task(Base):
    __tablename__ = 'Task'

    idTask = Column(Integer, primary_key=True, autoincrement=True)
    taskName = Column(String(255), nullable=False)
    estimedTime = Column(Integer, nullable=False)
    offer = Column(Integer, nullable=False)
    suggestedOffer = Column(Integer, nullable=False)
    userBalance = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
    direction = Column(String(255), nullable=False)

    def __repr__(self):
        return (f"<Task(idTask={self.idTask}, taskName={self.taskName}, estimedTime={self.estimedTime}, "
                f"offer={self.offer}, suggestedOffer={self.suggestedOffer}, userBalance={self.userBalance}, "
                f"date={self.date}, direction={self.direction})>")

