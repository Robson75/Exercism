def value(colors):
    """Return resistance value of a resistor"""

    color_values = {'black': 0,
                    'brown': 1,
                    'red': 2,
                    'orange': 3,
                    'yellow': 4,
                    'green': 5,
                    'blue': 6,
                    'violet': 7,
                    'grey': 8,
                    'white': 9}

    return int(str(color_values.get(colors[0])) + str(color_values.get(colors[1])))
