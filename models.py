from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(55), unique=True)
    email = Column(String(55), unique=True)
