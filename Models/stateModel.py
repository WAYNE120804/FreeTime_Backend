from sqlalchemy import Column, String, Integer, ForeignKey
from Models.init import Base

class State(Base):
    __tablename__ = 'State'

    state_id = Column(Integer, primary_key=True)
    state_name = Column(String(70), nullable=False)  # Longitud especificada
    country_id = Column(Integer,ForeignKey('Country.country_id')) #llave foranea de pais


    def __repr__(self):
        return (f"State(state_id={self.state_id}, state_name='{self.state_name}', country_id ={self.country_id} )>")