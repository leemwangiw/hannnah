import click
from app.database import SessionLocal, init_db
from app.views import add_user, add_location, show_weather_for_location

# Initialize database
init_db()

@click.group()
def cli():
    """Weather Forecast Application"""
    pass

@click.command()
@click.option('--username', prompt='Your username', help='Enter your username.')
@click.option('--email', prompt='Your email', help='Enter your email.')
def create_user(username, email):
    """Create a new user."""
    session = SessionLocal()
    add_user(session, username, email)
    session.close()

@click.command()
@click.option('--username', prompt='Your username', help='Enter your username.')
@click.option('--location', prompt='Location name', help='Enter location to save.')
def add_location_cmd(username, location):
    """Add a new location."""
    session = SessionLocal()
    add_location(session, username, location)
    session.close()

@click.command()
@click.option('--location', prompt='Location name', help='Enter location to view weather.')
def show_weather(location):
    """Show current weather for a location."""
    session = SessionLocal()
    show_weather_for_location(session, location)
    session.close()

# Register commands to the CLI
cli.add_command(create_user)
cli.add_command(add_location_cmd)
cli.add_command(show_weather)

if __name__ == '__main__':
    cli()
