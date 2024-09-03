from sqlalchemy import Column, Integer, String
from Models.init import Base

class Bank(Base):
    __tablename__ = 'Bank'

    Bank_id = Column(Integer, primary_key=True)
    Bank_name = Column(String(50))  

    def __repr__(self):
        return (f"<Bank(Bank_id={self.Bank_id}, "
          f"Bank_name='{self.Bank_name}')>")
