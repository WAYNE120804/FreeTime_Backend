from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .userModel import User
from .chargeModel import Charge
from .roleModel import Role
from .usersOffersModel import UsersOffers