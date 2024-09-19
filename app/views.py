from app.database import SessionLocal
from app.models import User, Location, WeatherHistory
from app.weather_data import generate_weather_data

def add_user(session, username, email):
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    print(f"User {username} added!")

def add_location(session, username, location_name):
    user = session.query(User).filter_by(username=username).first()
    if not user:
        print(f"User {username} not found!")
        return

    location = Location(name=location_name, user=user)
    session.add(location)
    session.commit()
    print(f"Location {location_name} added for user {username}.")

def show_weather_for_location(session, location_name):
    location = session.query(Location).filter_by(name=location_name).first()
    if not location:
        print(f"Location {location_name} not found!")
        return

    weather = generate_weather_data()
    weather_record = WeatherHistory(location=location, temperature=weather['temperature'], conditions=weather['conditions'])
    session.add(weather_record)
    session.commit()

    print(f"Current Weather for {location_name}: {weather['temperature']} and {weather['conditions']}")
