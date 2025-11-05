from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    skills = Column(JSON)
    past_projects = Column(JSON, default=[])

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    required_skills = Column(JSON)
    status = Column(String)
