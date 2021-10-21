def prime_sieve(max_n):
    numbers = list(range(2, max_n + 1))
    primes = []
    while len(numbers):
        primes.append(numbers[0])
        numbers = [number for number in numbers if number % numbers[0] != 0]
    return primes


num = 600851475143
for factor in prime_sieve(int(num ** 0.5))[::-1]:
    if num % factor == 0:
        print(factor)
        break
