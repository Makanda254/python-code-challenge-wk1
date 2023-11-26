def two_numbers_are_positive(num1, num2, num3):
    positive_count = 0

    if num1 > 0:
        positive_count += 1
    if num2 > 0:
        positive_count += 1
    if num3 > 0:
        positive_count += 1

    return positive_count == 2

print(two_numbers_are_positive(1, 2, 3))