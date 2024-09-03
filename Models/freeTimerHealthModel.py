from sqlalchemy import Column, String, Integer, DateTime,BLOB, ForeignKey
from Models.init import Base

class FreeTimerHealth(Base):
    __tablename__ = 'FreeTimerHealth'

    freeTimer_health_id = Column(Integer, primary_key=True)
    freeTimer_health_date_start = Column(DateTime, nullable=False)  # Longitud especificada
    freeTimer_health_date_update = Column(DateTime, nullable=False) 
    freeTimer_health_date_end = Column(DateTime, nullable=False) 
    freeTimer_health_date_document = Column(BLOB, nullable=False) 
    user_id = Column(Integer, ForeignKey('User.user_id'))#llave foranea del id del usuario


    def __repr__(self):
        return (f"FreeTimerHealth(freeTimer_health_id={self.freeTimer_health_id}, freeTimer_health_date_start='{self.freeTimer_health_date_start}',"
                f" freeTimer_health_date_update='{self.freeTimer_health_date_update}', freeTimer_health_date_end='{self.freeTimer_health_date_end}' "
                f" user_id='{self.user_id}' )>")