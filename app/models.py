from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False)
    locations = relationship('Location', back_populates='user')

class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='locations')
    weather_history = relationship('WeatherHistory', back_populates='location')

class WeatherHistory(Base):
    __tablename__ = 'weather_history'
    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey('locations.id'))
    location = relationship('Location', back_populates='weather_history')
    date = Column(DateTime, default=datetime.utcnow)
    temperature = Column(String, nullable=False)
    conditions = Column(String, nullable=False)
