from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


from .taskModel import Task
from .paymentModel import Payment
from .fullTimerModel import FullTimer
from .administratorModel import Administrator
from .userModel import Users
from .supportModel import Support