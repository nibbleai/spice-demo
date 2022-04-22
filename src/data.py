import pandas as pd

from src.columns import PICKUP_TIME, DROPOFF_TIME, WEATHER_DATE

ROOT_URL = "https://nibble-datasets.s3.eu-west-1.amazonaws.com/nyc-taxi/"
TRIPS_FILENAME = "nyc-taxi-2015.csv"
WEATHER_FILENAME = "nyc-weather-2015.csv"

__all__ = ["load_trips", "load_weather"]


def load_trips():
    return pd.read_csv(
        f"{ROOT_URL}{TRIPS_FILENAME}",
        parse_dates=[PICKUP_TIME, DROPOFF_TIME],
    )


def load_weather():
    return pd.read_csv(
        f"{ROOT_URL}{WEATHER_FILENAME}",
        parse_dates=[WEATHER_DATE],
    )
