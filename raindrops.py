def convert(number):
    sound = ""
    has_factor = False
    if number % 3 == 0:
        sound += "Pling"
        has_factor = True
    if number % 5 == 0:
        sound += "Plang"
        has_factor = True
    if number % 7 == 0:
        sound += "Plong"
        has_factor = True
    if not has_factor:
        sound = str(number)
    return sound
