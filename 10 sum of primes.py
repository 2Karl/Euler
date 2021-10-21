import time

def prime_sieve(max_n):
    numbers = [2] + list(range(3, max_n + 1, 2))
    primes = []
    while numbers[0] <= max_n**0.5:
        primes.append(numbers[0])
        numbers = [number for number in numbers if number % numbers[0] != 0]
    primes += numbers
    return primes

start = time.perf_counter()
print(sum(prime_sieve(100000000)))
print(time.perf_counter()-start)