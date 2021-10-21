import math
import time


def sieve(n):
    numbers = [2] + list(range(3, n + 1, 2))
    s_primes = []
    while numbers:
        if numbers[0] > int(n ** 0.5):
            s_primes += numbers
            numbers = []
        else:
            s_primes.append(numbers[0])
            numbers = [x for x in numbers if x % numbers[0] != 0]
    return s_primes


def prime_factors(n):
    # primes = sieve(n)
    factors = []
    while n > 1:
        for prime in primes:
            if n % prime == 0:
                n //= prime
                factors.append(prime)
                break
            if prime > n ** 0.5:
                factors.append(n)
                n = 1
                break
    return factors


def count_factors(n):
    p_factors = prime_factors(n)
    return math.prod(p_factors.count(x) + 1 for x in set(p_factors))


def triangular_numbers():
    n = 0
    addend = 1
    while True:
        n += addend
        yield n
        addend += 1


# quicker to generate all the primes below 1 million in one go for use in factorisation
# than to generate them for each number being factorised
start = time.perf_counter()
primes = sieve(100000)
nums = triangular_numbers()
t_num = next(nums)
while count_factors(t_num) <= 500:
    t_num = next(nums)
print(t_num)
print(time.perf_counter() - start)
