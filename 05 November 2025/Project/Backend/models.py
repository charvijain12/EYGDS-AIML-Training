# models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import JSON
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    skills = Column(JSON)
    past_projects = Column(JSON, default=[])

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    required_skills = Column(JSON)
    status = Column(String, default="open")