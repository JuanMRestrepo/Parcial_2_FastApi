import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()
#Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

#Create the engine that manages the db connection
engine = create_engine(DATABASE_URL)
#create the session which is used to perform operations on the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Create a base class from which database model classes will derive.
Base = declarative_base()

def get_db():
    """
    Method that creates a dependency to manage the database session
    :return: db
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()