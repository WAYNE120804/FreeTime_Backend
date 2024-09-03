from sqlalchemy import Column, Integer, String
from Models.init import Base

class Bank(Base):
    __tablename__ = 'Bank'

    bank_id = Column(Integer, primary_key=True)
    bank_name = Column(String(50))  

    def __repr__(self):
        return (f"<Bank(bank_id={self.bank_id}, "
          f"bank_name='{self.bank_name}')>")
