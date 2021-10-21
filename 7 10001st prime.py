import time

def prime_sieve(max_n):
    numbers = list(range(2, max_n + 1))
    primes = []
    while len(numbers):
        primes.append(numbers[0])
        numbers = [number for number in numbers if number % numbers[0] != 0]
    return primes

start = time.perf_counter()
print(prime_sieve(110000)[10000])
print(time.perf_counter()-start)