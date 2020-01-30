SECONDS_PER_YEAR = 31557600
earth_years = {'Earth': 1,
               'Mercury': 0.2408467,
               'Venus': 0.61519726,
               'Mars': 1.8808158,
               'Jupiter': 11.862615,
               'Saturn': 29.447498,
               'Uranus': 84.016846,
               'Neptune': 164.79132}


def calculate_years(planet, seconds):
    return round((seconds / SECONDS_PER_YEAR) / earth_years.get(planet), 2)


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return calculate_years('Earth', self.seconds)

    def on_mercury(self):
        return calculate_years('Mercury', self.seconds)

    def on_venus(self):
        return calculate_years('Venus', self.seconds)

    def on_mars(self):
        return calculate_years('Mars', self.seconds)

    def on_jupiter(self):
        return calculate_years('Jupiter', self.seconds)

    def on_saturn(self):
        return calculate_years('Saturn', self.seconds)

    def on_uranus(self):
        return calculate_years('Uranus', self.seconds)

    def on_neptune(self):
        return calculate_years('Neptune', self.seconds)
