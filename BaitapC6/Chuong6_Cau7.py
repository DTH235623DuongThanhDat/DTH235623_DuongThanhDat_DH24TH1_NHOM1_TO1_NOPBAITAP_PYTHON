n = int(input("Nhập số phần tử của dãy: "))

day = []  

for i in range(n):
    while True:
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        if i > 0 and x <= day[i - 1]:
            print("Số bạn nhập không theo thứ tự tăng, vui lòng nhập lại!")
        else:
            day.append(x)
            break

print("✅ Dãy số đã nhập theo thứ tự tăng dần là:")
print(day)