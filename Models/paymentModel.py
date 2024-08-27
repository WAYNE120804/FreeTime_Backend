from sqlalchemy import Column, Integer, String, Enum
from Models.init import Base
import enum

class AccountType(enum.Enum):
    AHORRO = "Ahorro"
    CORRIENTE = "Corriente"
    CREDITO = "Credito"

class Payment(Base):
    __tablename__ = 'Payments'

    idPayment = Column(Integer, primary_key=True, autoincrement=True)
    accountNumber = Column(String(255), nullable=False)
    accountHolder = Column(String(255), nullable=False)
    accountType = Column(Enum(AccountType), nullable=False)

    def __repr__(self):
        return (f"<Payments(idPayment={self.idPayment}, accountNumber={self.accountNumber}, "
                f"accountHolder={self.accountHolder}, accountType={self.accountType})>")