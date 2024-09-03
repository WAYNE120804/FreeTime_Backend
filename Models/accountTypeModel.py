from sqlalchemy import Column, Integer, String
from Models.init import Base

class Account_Type(Base):
    __tablename__ = 'Account_Type'

    account_Type_id = Column(Integer, primary_key=True)
    account_Type_name = Column(String(50))  # Asumiendo que el límite es 50 caracteres

    def __repr__(self):
        return (f"<Account_Type(account_Type_id={self.account_Type_id}, "
        f"account_Type_name='{self.account_Type_name}')>")
