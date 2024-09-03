from sqlalchemy import Column, Integer, String, DateTime
from Models.init import Base

class Task(Base):
    __tablename__ = 'Tasks'

    task_id = Column(Integer, primary_key=True)
    task_start_date = Column(DateTime)
    task_end_date = Column(DateTime)
    task_offer_suggested = Column(String(400))
    task_description = Column(String(400))
    address = Column(String(50))
    price_offer_id = Column(Integer)
    task_type_id = Column(Integer)

    def __repr__(self):
        return (f"<Task(task_id={self.task_id}, "
                f"task_start_date={self.task_start_date}, "
                f"task_end_date={self.task_end_date}, "
                f"task_offer_suggested={self.task_offer_suggested}, "
                f"task_description={self.task_description}, "
                f"address={self.address}, "
                f"price_offer_id={self.price_offer_id}, "
                f"task_type_id={self.task_type_id})>")