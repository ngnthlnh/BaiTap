n=int(input("So tien ban dau: "))
#nhập vào số tiền ban đầu 
k=int(input("So thang gui: "))
#nhập vào số tháng gửi
T=float(input("Lai suat/thang: "))
#nhập vào lãi suất của một tháng 
print("Voi so tien ban dau " + str(n) + ", sau " + str(k) + " thang gui, lai suat " + str(T) + "/thang")
#in lên màn hình câu "Với số tiền ban đầu n, sau k tháng gửi, lãi suất là T/tháng"
print("Thi so tien nhan duoc cuoi ky la: ", str(n*(1+k*T)))
#In lên màn hình câu "thì số tiền nhận được cuối kỳ là..."