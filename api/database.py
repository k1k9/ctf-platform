from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Setting up connection based on env vars
host = environ.get('DATABASE_HOST')
user = environ.get('DATABASE_USER')
password = environ.get('DATABASE_PASSWORD') if environ.get('DATABASE_PASSWORD') != None else ""
port = environ.get('DATABASE_PORT')
name = environ.get('DATABASE_NAME')

url_database = f"mysql+mysqldb://{user}:{password}@{host}:{port}/{name}"

engine = create_engine(
    url_database
)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()