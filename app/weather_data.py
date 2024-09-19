import random

# Simulating weather data
def generate_weather_data():
    temperatures = ["20°C", "25°C", "18°C", "30°C", "15°C"]
    conditions = ["Sunny", "Rainy", "Cloudy", "Windy", "Snowy"]
    
    return {
        "temperature": random.choice(temperatures),
        "conditions": random.choice(conditions),
    }
