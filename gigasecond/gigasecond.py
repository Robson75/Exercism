from datetime import timedelta


def add(moment):
    # moment is a datetime object
    seconds_passed = 10 ** 9
    new_moment = moment + timedelta(seconds=seconds_passed)
    return new_moment
