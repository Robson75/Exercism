def is_armstrong_number(number):
    digits = len(str(number))
    sum_ = sum(int(i) ** digits for i in str(number))
    return sum_ == number

