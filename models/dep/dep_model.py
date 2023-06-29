from models.database import Base
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import Column, Integer, String


class DbDep(Base):
    __tablename__ = "division"
    div_code = Column(Integer, primary_key=True, index=True)
    div_name = Column(String, nullable=True)
    div_shortname = Column(String, nullable=True)
    off_id = Column(String, nullable=True)
    div_sort = Column(Integer, nullable=True)

