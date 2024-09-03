from sqlalchemy import Column, Integer, DateTime, ForeignKey
from Models.init import Base

class Offer(Base):
    __tablename__ = 'Offer'

    offer_id = Column(Integer, primary_key=True)
    offer_date = Column(DateTime)
    offer_suggested_price = Column(Integer)
    user_id_freetime = Column(Integer, ForeignKey('User.user_id'))
    user_id1_fulltime = Column(Integer, ForeignKey('User.user_id'))
    offer_freetimer_calification = Column(Integer)
    offer_fulltimer_calification = Column(Integer)

    def __repr__(self):
        return (f"<Offer(offer_id={self.offer_id}, "
                f"offer_date={self.offer_date}, "
                f"offer_suggested_price={self.offer_suggested_price}, "
                f"user_id_freetime={self.user_id_freetime}, "
                f"user_id1_fulltime={self.user_id1_fulltime}, "
                f"offer_freetimer_calification={self.offer_freetimer_calification}, "
                f"offer_fulltimer_calification={self.offer_fulltimer_calification})>")