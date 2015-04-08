from datetime import timedelta


def add_gigasecond(date):
    diff = timedelta(seconds=10 ** 9)
    return date + diff