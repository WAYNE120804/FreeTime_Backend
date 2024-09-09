from sqlalchemy import Column, Integer, VARCHAR
from Models.init import Base

class AccountType(Base):
    __tablename__ = 'AccountType'

    account_Type_id = Column(Integer, primary_key=True)
    account_Type_name = Column(VARCHAR(20))  # Asumiendo que el límite es 50 caracteres

    def __repr__(self):
        return (f"<AccountType(account_Type_id={self.account_Type_id}, "
        f"account_Type_name='{self.account_Type_name}')>")
