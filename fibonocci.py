def generate_fibonacci(n):
    return n if n < 2 else generate_fibonacci(n - 1) + generate_fibonacci(n - 2)


print(generate_fibonacci(6))