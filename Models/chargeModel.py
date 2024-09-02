from sqlalchemy import Column, Integer, DateTime, DECIMAL, String
from Models.init import Base

class Charge(Base):
    __tablename__ = 'Charge'

    charge_id = Column(Integer, primary_key=True, autoincrement=True)
    charge_date = Column(DateTime, nullable=False)  # Fecha y hora de la carga
    charge_value = Column(Integer, nullable=False)  # Valor de la carga
    user_account = Column(DECIMAL, nullable=False)  # Cuenta del usuario como valor decimal
    charge_reference = Column(String(40), nullable=False)  # Referencia de la carga con longitud especificada
    user_id = Column(Integer, nullable=False)  # Campo para relación futura con la tabla Users

    def __repr__(self):
        return (f"<Charge(charge_id={self.charge_id}, charge_date='{self.charge_date}', "
                f"charge_value={self.charge_value}, user_account={self.user_account}, "
                f"charge_reference='{self.charge_reference}', user_id={self.user_id})>")