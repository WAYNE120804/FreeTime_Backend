from sqlalchemy import Column, Integer,ForeignKey
from Models.init import Base

class Account(Base):
    __tablename__ = 'Account'

    account_id = Column(Integer, primary_key=True)
    account_number = Column(Integer)
    bank_id = Column(Integer, ForeignKey('Bank.bank_id'))
    account_Type_id = Column(Integer, ForeignKey('Account_Type.account_Type_id'))

    def __repr__(self):
        return (f"<Account(account_id={self.account_id}, "
        f"account_number={self.account_number}, " 
        f"bank_id={self.bank_id}, "
        f"account_Type_id={self.account_Type_id})>")
