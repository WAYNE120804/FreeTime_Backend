from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Support(Base):
    __tablename__ = 'support'

    idSupport = Column(Integer, primary_key=True, autoincrement=True)
    nameRequestSupport = Column(String, nullable=False)
    emailRequestSupport = Column(String, nullable=False)
    descriptionTopic = Column(Text, nullable=False)
    topicToReport = Column(String, nullable=False)

    def __repr__(self):
        return (f"<Support(idSupport={self.idSupport}, nameRequestSupport='{self.nameRequestSupport}', emailRequestSupport='{self.emailRequestSupport}'>")
