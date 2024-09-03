from sqlalchemy import Column, String, Integer,ForeignKey
from Models.init import Base

class City(Base):
    __tablename__ = 'City'

    city_id = Column(Integer, primary_key=True)
    city_name = Column(String(70), nullable=False)  # Longitud especificada
    state_id = Column(Integer, ForeignKey('State.state_id')) # llave foranea del departemento


    def __repr__(self):
        return (f"City(City_id={self.city_id}, city_name='{self.city_name}, state_id={self.state_id}' )>")