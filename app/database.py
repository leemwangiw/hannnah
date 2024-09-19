from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Initialize the SQLite database
DATABASE_URL = "sqlite:///weather_forecast.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)
