def sum_n_times(n):
    sum = 0

    for x in range(0, n):
        sum = sum + x

    return sum

print(sum_n_times(13))