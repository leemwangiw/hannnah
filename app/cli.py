import click
# Step 1: Define a list of sample cities and their forecasts
CITIES = [
    {"city": "New York", "forecast": "Sunny, 25°C"},
    {"city": "Los Angeles", "forecast": "Cloudy, 20°C"},
    {"city": "London", "forecast": "Rainy, 18°C"},
    {"city": "Paris", "forecast": "Sunny, 22°C"},
    {"city": "Tokyo", "forecast": "Partly cloudy, 19°C"},
    {"city": "Sydney", "forecast": "Clear, 30°C"},
    {"city": "Berlin", "forecast": "Windy, 16°C"},
    {"city": "Moscow", "forecast": "Snowy, -5°C"},
    {"city": "Cairo", "forecast": "Hot, 35°C"},
    {"city": "Toronto", "forecast": "Cool, 15°C"}
]

# Step 2: Create the show-weather command
@click.command()
@click.option('--location', prompt='Location name', help='The location for which to show the weather.')
def show_weather(location):
    # Find the city's forecast
    city_forecast = next((city['forecast'] for city in CITIES if city['city'].lower() == location.lower()), None)

    if city_forecast:
        click.echo(f"The weather in {location} is: {city_forecast}")
    else:
        click.echo(f"Sorry, no forecast available for {location}")

# Step 3: Add the command to the CLI
if __name__ == "__main__":
    show_weather()
