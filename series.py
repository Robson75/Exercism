def slices(series, length):
    nr_of_digits = len(series)
    substrings = []
    if nr_of_digits < length:
        raise ValueError("The series of numbers is not that long.")
    elif length <= 0:
        raise ValueError("The length of the substring most be at least 1.")
    else:
        i = 0
        while i + length <= nr_of_digits:
            substrings.append(series[i:i + length])
            i += 1
    return substrings
