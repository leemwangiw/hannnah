# Weather Forecast Application

## Description

A command-line interface (CLI) application for managing weather forecasts. This tool allows users to add new locations, create new users, and view current weather information for specific locations.

## Installation

Follow these steps to get your development environment set up:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/weather-forecast-app.git
    cd weather-forecast-app
    ```

2. **Set up a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

    If you don't have a `requirements.txt` file, you can install the required packages manually:

    ```bash
    pip install sqlalchemy click
    ```

## Usage

To use the CLI application, run the `cli.py` script with the following command:

```bash
python3 app/cli.py [OPTIONS] COMMAND [ARGS]...
