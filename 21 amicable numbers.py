def prime_sieve(max_n):
    numbers = [2] + list(range(3, max_n + 1, 2))
    primes = []
    while numbers[0] <= max_n**0.5:
        primes.append(numbers[0])
        numbers = [number for number in numbers if number % numbers[0] != 0]
    primes += numbers
    return primes

def is_prime(n):
    return n in primes

def amicable(n, p, q, r):
    return (2**n*p*q, 2**n*r)

primes = prime_sieve(1000000)


# for n in range(1, 1000):
#   for m in range(1, n):
#     p = (2**(n-m)+1)*2**m-1
#     if is_prime(p):
#
#         q = (2**(n-m)+1)*2**n-1
#         if is_prime(q):
#
#             r=(2**(n-m)+1)**2*2**(m+n)-1
#             if is_prime(r):
#
#                 print(n, m)
#                 print(amicable(n, p, q, r))