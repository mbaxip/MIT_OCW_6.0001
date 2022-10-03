def fibonacci(n):
    # Base case
    if n == 0 or n == 1:
        return n

    else:
        return fibonacci(n-2) + fibonacci(n-1)

n = 10
for i in range(0,n):
    print(fibonacci(i), end=" ")
