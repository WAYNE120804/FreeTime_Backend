from sqlalchemy import Column, Integer, String, Text
from Models.init import Base

class Support(Base):
    __tablename__ = 'Support'

    idSupport = Column(Integer, primary_key=True, autoincrement=True)
    nameRequestSupport = Column(String(255), nullable=False)  # Longitud especificada
    emailRequestSupport = Column(String(255), nullable=False) # Longitud especificada
    descriptionTopic = Column(Text, nullable=False)  # Text no requiere longitud
    topicToReport = Column(String(255), nullable=False)  # Longitud especificada

    def __repr__(self):
        return (f"<Support(idSupport={self.idSupport}, nameRequestSupport='{self.nameRequestSupport}', "
                f"emailRequestSupport='{self.emailRequestSupport}', descriptionTopic='{self.descriptionTopic}', "
                f"topicToReport='{self.topicToReport}')>")