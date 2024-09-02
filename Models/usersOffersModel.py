from sqlalchemy import Column, Integer
from Models.init import Base

class UsersOffers(Base):
    __tablename__ = 'UsersOffers'

    user_offer_id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, nullable=False)  # ID del rol (llave foránea)
    offer_id = Column(Integer, nullable=False)  # ID de la oferta (llave foránea)

    def __repr__(self):
        return f"<UsersOffers(user_offer_id={self.user_offer_id}, role_id={self.role_id}, offer_id={self.offer_id})>"