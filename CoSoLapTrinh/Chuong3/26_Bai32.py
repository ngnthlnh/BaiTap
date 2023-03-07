m1=int(input('M1='))
m2=int(input('M2='))
m3=int(input('M3='))
s=int(input('S='))
tra=int(0)
if 1 <= s <= 100 :
    tra=s*m1
elif 100 < s <= 150 :
    tra=100*m1+(s-100)*m2
else: tra=100*m1+50*m2+(s-150)*m3
print("Phai tra=",tra,sep=(""))