def sum_factors(n):
    return sum(sum([i, n // i]) for i in range(2, int(n ** 0.5) + 1) if n % i == 0) + 1


print(sum(i for i in range(220, 10000) if sum_factors(sum_factors(i)) == i != sum_factors(i)))
