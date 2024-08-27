from sqlalchemy import Column, Integer, String, Enum
from Models.init import Base

class Reward(Base):
    __tablename__ = 'Rewards'

    idReward =Column(Integer, primary_key=True, autoincrement=True)
    jobsDone = Column(Integer, nullable=False)
    timeAsFreeTimer = Column(Integer, nullable=False)
    positiveRatings = Column(Integer, nullable=False)

    def __repr__(self):
        return(f"<Rewards(idRewards={self.idReward}, "
               f"jobsDone={self.jobsDone}, timeAsFreeTimer={self.timeAsFreeTimer}, "
               f"positiveRatings={self.positiveRatings})>")