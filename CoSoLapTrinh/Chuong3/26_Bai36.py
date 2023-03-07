a=float(input(""))
b=float(input(""))
c=float(input(""))
if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0 :
    if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2 :
        print("Tam giac vuong")
    elif a==b and c==b and c==a :
        print("Tam giac deu")
    else: 
        print("Tam giac loai khac")
else:
    print("Khong hop le")