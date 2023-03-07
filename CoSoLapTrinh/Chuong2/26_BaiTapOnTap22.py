a=int(input("Nhap Gia niem yet: "))
b=int(input("Nhap Chiet khau: "))
VAT=float((a-b)*0.01)
print("Gia ban: " + str(float(a-b+VAT)))