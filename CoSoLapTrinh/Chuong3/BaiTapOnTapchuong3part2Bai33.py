n = int(input())
if n > 9:
    print('chi tinh duoc tu 1 den 9')
else:
    i = 1
    while i <= 9:
        print('{} x {} = {}'.format(n, i , n * i))
        i += 1