from sqlalchemy import Column, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Support(Base):
    __tablename__ = 'support'

    nameRequestSupport = Column(String, nullable=False)
    emailRequestSupport = Column(String, nullable=False)
    descriptionTopic = Column(Text, nullable=False)
    topicToReport = Column(String, nullable=False)

    def __repr__(self):
        return f"<Support(nameRequestSupport='{self.nameRequestSupport}', emailRequestSupport='{self.emailRequestSupport}')>"
