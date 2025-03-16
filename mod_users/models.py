from app import db
from sqlalchemy import Column, Integer, String


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    role = Column(Integer, nullable=False, default=0)
    full_name = Column(String(32))
