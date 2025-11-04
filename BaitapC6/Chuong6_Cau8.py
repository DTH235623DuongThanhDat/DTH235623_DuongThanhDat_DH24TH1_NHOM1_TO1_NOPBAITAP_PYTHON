n = int(input("Nhập số lượng phần tử n: "))

# Nhập dãy số thực
M = []
for i in range(n):
    x = float(input(f"Nhập M[{i}]: "))
    M.append(x)

# Sắp xếp dãy theo thứ tự giảm dần
M.sort(reverse=True)

# Xuất kết quả
print("Dãy sau khi sắp xếp giảm dần:")
for i in range(n):
    print(M[i], end=" ")