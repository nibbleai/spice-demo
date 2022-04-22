from src.config import TARGET
from src.columns import PICKUP_TIME, DROPOFF_TIME


def create_target(trips):
    return (trips[DROPOFF_TIME] - trips[PICKUP_TIME]).dt.seconds


def preprocess(trips):
    return trips.assign(**{TARGET: create_target})
