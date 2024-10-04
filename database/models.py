from sqlalchemy import Column, Integer, DateTime

from database import Base
from datetime import datetime


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    create_on = Column(DateTime, default=datetime.now)
    update_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)


# class PatternManage(Base)
