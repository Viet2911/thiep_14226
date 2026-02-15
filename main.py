a = int(input("Hãy nhập vào số a: "))
b = int(input("Hãy nhập vào số b: "))
pheptinh = input("Hãy nhập phép tính (+, -, *, /): ")
if pheptinh == "+":
    ketqua = a + b
    print("Kết quả của phép cộng là:", ketqua)
if pheptinh == "-":
    ketqua = a - b
    print("Kết quả của phép trừ là:", ketqua)
if pheptinh == "*":
    ketqua = a * b
    print("Kết quả của phép nhân là:", ketqua)
if pheptinh == "/":
    ketqua = a / b
    print("Kết quả của phép chia là:", ketqua)