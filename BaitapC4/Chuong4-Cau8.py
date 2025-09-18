import math

a = float(input("Nhập cơ số a (a > 0, a != 1): "))
x = float(input("Nhập số x (x > 0): "))
if x > 0 and a > 0 and a != 1:
	loga_x = math.log(x) / math.log(a)
	print(f"log_{a}({x}) = {loga_x}")
else:
    print("Giá trị nhập không hợp lệ (x > 0, a > 0, a != 1).")
