from sqlalchemy import Column, Integer, String, Enum
from Model.init import Base
import enum

class AccountType(enum.Enum):
    AHORRO = "ahorro"
    CORRIENTE = "corriente"
    CREDITO = "credito"

class Payment(Base):
    __tablename__ = 'payment'

    idPayment = Column(Integer, primary_key=True, autoincrement=True)
    accountNumber = Column(String(255), nullable=False)
    accountHolder = Column(String(255), nullable=False)
    accountType = Column(Enum(AccountType), nullable=False)

    def __repr__(self):
        return (f"<Payment(idPayment={self.idPayment}, accountNumber={self.accountNumber}, "
                f"accountHolder={self.accountHolder}, accountType={self.accountType})>")