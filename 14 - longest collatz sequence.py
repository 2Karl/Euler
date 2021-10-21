def collatz(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return len(sequence)


print(max([[collatz(x), x] for x in range(1, 1000000)], key=lambda x: x[0])[1])
