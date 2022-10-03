def mult(n, num):
    # Base case:
    if n == 0 or n == 1:
        return n * num

    else:
        return num + mult(n-1, num)

print(mult(4, 3))
