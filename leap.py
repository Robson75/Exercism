def leap_year(year):
    if year % 4 != 0:
        return False
    else:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
    return True
