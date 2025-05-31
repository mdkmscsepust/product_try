import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

DATABASE_URL=f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

# Define a base class
Base = declarative_base()