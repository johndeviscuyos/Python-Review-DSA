def diamond(n):
    if n % 2 == 0:
        return

    for i in range(n):
        spaces = abs(n // 2 - i)
        stars = n - 2 * spaces
        print(' ' * spaces + '*' * stars)


print(diamond(9))
