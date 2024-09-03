from sqlalchemy import Column, String, Integer, Boolean, BLOB, ForeignKey
from Models.init import Base

class User(Base):
    __tablename__ = 'User'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_full_name = Column(String(70), nullable=False)  # Longitud especificada
    user_address = Column(String(50), nullable=True)  # Longitud especificada
    user_email = Column(String(50), unique=True, nullable=False)  # Longitud especificada y único
    user_nickname = Column(String(20), nullable=True)  # Longitud especificada
    user_document = Column(String(10), unique=True, nullable=False)  # Longitud especificada y único
    user_password = Column(String(255), nullable=False)  # Longitud especificada para la contraseña
    user_photo = Column(BLOB, nullable=True)  # BLOB para almacenar fotos
    user_enable = Column(Boolean, default=False)  # TINYINT puede ser mapeado como Boolean en SQLAlchemy
    user_points = Column(Integer, default=0)  # Puntos del usuario
    user_phone_number = Column(Integer, nullable=True)  # Número de teléfono
    role_id = Column(Integer, ForeignKey('Role.role_id'))  # Campo para relación futura con tabla Roles
    city_id = Column(Integer, ForeignKey('City.city_id'))  # Campo para relación futura con tabla City
    account_id = Column(Integer, nullable=True)  # Campo para relación futura con tabla Account

    def __repr__(self):
        return (f"<User(user_id={self.user_id}, user_full_name='{self.user_full_name}', "
                f"user_email='{self.user_email}', user_nickname='{self.user_nickname}', "
                f"user_document='{self.user_document}', user_enable={self.user_enable}, "
                f"user_points={self.user_points}, user_phone_number={self.user_phone_number})>")