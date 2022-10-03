def sum_numbers(numbers):
    # Base case
    if len(numbers) == 1:
        return numbers[0]

    else:
        return numbers[0] + sum_numbers(numbers[1:])

nums = [1, 4, 6, 10]
print(sum_numbers(nums))
