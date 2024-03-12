def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

def is_fibonacci(n):
    fib_series = [0, 1]
    if n in fib_series:
        return True
    while fib_series[len(fib_series) - 1] <= n:
        if n in fib_series:
            return True
        else:
            fib_series.append(fib_series[-1] + fib_series[-2])
    return False

num = 0
print(f'is {num} in fibonacci')
print(fibonacci(num / 3))
print(is_fibonacci(num))
