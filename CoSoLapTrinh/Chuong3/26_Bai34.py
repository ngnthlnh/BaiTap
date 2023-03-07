toan=int(input()) #diem toan, he so 2
ly=int(input()) #diem ly, he so 3
anh=int(input()) #diem anh 
TB=float((toan*2 + ly*3 + anh)/6)
if TB < 3:
    print('Kem')
elif 3 <= TB < 5:
    print('Yeu')
elif 5 <= TB < 6:
    print('Trung binh')
elif 6 <= TB < 7:
    print('Trung binh Kha')
elif 7 <= TB < 8:
    print('Kha')
elif 8 <= TB < 9:
    print('Gioi')
elif 9 <= TB < 10:
    print('Xuat sac')
    