print(sum(x**2 for x in range(1, 11)))
print(sum(x for x in range(1, 11)) ** 2)
print(sum(x for x in range(1, 101)) ** 2 - sum(x**2 for x in range(1, 101)))