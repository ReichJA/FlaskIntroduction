import sys

# for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String, Float

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

# for configuration
from sqlalchemy import create_engine

# create declarative_base instance
Base = declarative_base()


# we create the class Project_Work and extend it from the Base Class.
class Project_Work(Base):
    __tablename__ = 'project_work'

    #Project ID
    id = Column(Integer, primary_key=True)
    #Project ID
    project = Column(String(200), unique=False, nullable=False)
    #what have I been working on?       
    content = Column(String(200), unique=False, nullable=False)       
    #when did I start my work?
    date_start = Column(String(10), unique=False, nullable=False)     
    time_start  = Column(String(6), unique=False, nullable=False)
    #when did I finish my work?
    date_end = Column(String(10), unique=False, nullable=False)       
    time_end  = Column(String(6), unique=False, nullable=False)
    #how long did it take?
    time = Column(Float, unique=False, nullable=False) 

# we create the class Projects and extend it from the Base Class.
class Projects(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)

    name = Column(String(200), unique=False, nullable=False)   
    time = Column(Float, unique=False, nullable=False)
    description = Column(String(200), unique=False, nullable=False) 

# we create the class working_type and extend it from the Base Class.
class Working_Type(Base):
    __tablename__ = 'working_type'

    id = Column(Integer, primary_key=True)

    name = Column(String(200), unique=False, nullable=False) 
    time = Column(Float, unique=False, nullable=False)


# creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///time-clock2.db')

Base.metadata.create_all(engine)