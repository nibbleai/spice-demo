from sklearn.model_selection import train_test_split as train_test_split_sk

from src.columns import PICKUP_TIME
from src.config import TARGET, TEST_SIZE


def train_test_split(trips):
    return train_test_split_sk(
        trips.sort_values(PICKUP_TIME),
        test_size=TEST_SIZE,
    )


def split_target(trips):
    y = trips[TARGET]
    X = trips.drop(columns=[TARGET])
    return X, y
