from sqlalchemy import Column, Integer, String, DateTime, DECIMAL,ForeignKey,VARCHAR
from Models.init import Base

class PayCheck(Base):
    __tablename__ = 'PayCheck'

    pay_check_id = Column(Integer, primary_key=True)
    pay_check_date = Column(DateTime)
    pay_check_value = Column(DECIMAL)
    offer_id = Column(Integer,ForeignKey('Offer.offer_id'))

    def __repr__(self):
        return (f"<PayCheck(pay_check_id={self.pay_check_id}, "
                f"pay_check_date={self.pay_check_date}, "
                f"pay_check_value={self.pay_check_value}, "
                f"offer_id={self.offer_id})>")
