from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


from .task import Task
from .payment import Payment