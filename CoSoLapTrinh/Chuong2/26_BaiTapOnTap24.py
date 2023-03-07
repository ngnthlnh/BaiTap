a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
s=float((a+b+c)/2)
import math
print("Dien tich=" + str(float(math.sqrt(s*(s-a)*(s-b)*(s-c)))))