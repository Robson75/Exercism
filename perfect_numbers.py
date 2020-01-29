def classify(number):
    print(number)
    if number <= 0:
        raise ValueError("Classification is only used for positive integers.")
    else:
        upper_limit = round(number/2) + 1
        factors = [i for i in range(1, upper_limit) if number % i == 0]
        aliquot_sum = sum(factors)
        print(aliquot_sum)
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"

