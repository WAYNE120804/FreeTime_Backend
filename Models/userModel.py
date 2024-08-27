from sqlalchemy import Column, String, Integer, Boolean
from Models.init import Base

class User(Base):
    __tablename__ = 'User'

    idUser = Column(Integer, primary_key=True, autoincrement=True)
    fullName = Column(String(255), nullable=False)  # Especificar longitud
    identification = Column(String(50), unique=True, nullable=False)  # Longitud especificada y único
    email = Column(String(255), unique=True, nullable=False)  # Especificar longitud y único
    phoneNumber = Column(String(20), nullable=True)  # Longitud especificada para número de teléfono
    country = Column(String(100), nullable=False)  # Longitud especificada
    city = Column(String(100), nullable=False)  # Longitud especificada
    address = Column(String(255), nullable=True)  # Longitud especificada
    freeTimer = Column(Boolean, default=False)
    fullTimer = Column(Boolean, default=False)
    password = Column(String(255), nullable=False)  # Longitud especificada para la contraseña
    balance = Column(Integer, default=0)

    def __repr__(self):
        return (f"<User(idUser={self.idUser}, fullName='{self.fullName}', email='{self.email}', "
                f"phoneNumber='{self.phoneNumber}', country='{self.country}', city='{self.city}', "
                f"address='{self.address}', freeTimer={self.freeTimer}, fullTimer={self.fullTimer}, "
                f"balance={self.balance})>")