height = 9
i = 0
while i < height:
    j = 0
    while j < height - i - 1:
        print(' ', end='')
        j += 1
    j = 0
    while j < 2 * i + 1:
        print('*', end='')
        j += 1
    print()
    i += 1
