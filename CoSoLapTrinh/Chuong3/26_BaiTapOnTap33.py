numberOfKW=int(input('Tieu thu='))
gia1=550
gia2=750
gia3=950
gia4=1350

money=float(0)
vat=float(0.1)
total=float(0)

if 1 <= numberOfKW <= 100:
  money = numberOfKW * gia1
elif 100 < numberOfKW <= 150:
  money = 100*gia1 + (numberOfKW - 100)*gia2 
elif 150 < numberOfKW <= 200:
  money = 100*gia1 + 50*gia2 + (numberOfKW - 150)*gia3
else:
  money = 100*gia1 + 50*gia2 + 50*gia3 + (numberOfKW - 200)*gia4
  
total = money + money*vat
print('Phai tra=',total,sep=(''))