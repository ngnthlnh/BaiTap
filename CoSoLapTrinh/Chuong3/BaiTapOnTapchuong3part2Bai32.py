n=int(input('n='))
if 1 <= n <= 50 :
    i=a=1
    while i<=n:
        print(i,end=(' '))
        if i%10==0:
            if i==10*a:
                print()
                print(sep=(''))
                a=a+1
        i=i+1