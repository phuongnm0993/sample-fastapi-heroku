import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://muntxahbgtwrqz:f99f794965dfb50888dd660a229b6028e31bde5c94a14662d63efe15749d2d80@ec2-18-234-17-166.compute-1.amazonaws.com:5432/dbe748dmk1khhs"
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()