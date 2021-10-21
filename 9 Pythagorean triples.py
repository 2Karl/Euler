import math

def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

def coprime(a, b):
  return gcd(a, b) == 1

def pythagorean_triple(m, n, k=1):
  return (k*(m**2 - n**2), k*(2*m*n), k*(m**2+n**2))

def both_odd(a, b):
  return a%2 == b%2 == 1


for n in range(1, 30):
  for m in range(n+1, 30):
    if coprime(m, n) and not both_odd(m, n):
      triple = pythagorean_triple(m,n)
      if 1000 % sum(triple) == 0:
          triple = pythagorean_triple(m, n, 1000//sum(triple))
          print(math.prod(triple))
          break