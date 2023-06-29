from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from sqlalchemy.sql import func

from models.database import Base
from pydantic import BaseModel
from typing import Optional


class DbUser(Base):
    __tablename__ = "member"
    pid = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    # password = Column(String)
    t_name = Column(String)
    f_name = Column(String)
    s_name = Column(String)
    position = Column(String)
    off_id = Column(String)
    div_code = Column(Integer)
    person_email = Column(String)
    person_tel = Column(String)
    person_fax = Column(String)
    status_id = Column(String)
    comment = Column(String)
    date_register = Column(DateTime)
    date_approve = Column(DateTime)


class UserBase(BaseModel):
    pid: int
    username: str
    t_name: str
    f_name: str
    s_name: str
    position: str
    off_id: str
    div_code: int
    person_email: str
    person_tel: str
    person_fax: str
    status_id: str
    comment: str
    date_register: Optional[datetime] = None
    date_approve: Optional[datetime] = None

    class Config:
        orm_mode = True

