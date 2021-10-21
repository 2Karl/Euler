import math
import time


def prime_sieve(max_n):
    numbers = list(range(2, max_n + 1))
    primes = []
    while len(numbers):
        primes.append(numbers[0])
        numbers = [number for number in numbers if number % numbers[0] != 0]
    return primes


def prime_factors(n, primes):
    factors = []
    while n > 1:
        for factor in primes:
            if n % factor == 0:
                factors.append(factor)
                n //= factor
                break
    return factors


num = 20
start = time.perf_counter_ns()

primes = prime_sieve(num)
print("Time to generate primes: " + str(time.perf_counter_ns() - start) + "ns")
start = time.perf_counter_ns()
print(math.prod(p ** max(f.count(p) for f in [prime_factors(x, primes) for x in range(2, num + 1)]) for p in primes))
print("Time to calculate LCM: " + str(time.perf_counter_ns() - start) + "ns")
