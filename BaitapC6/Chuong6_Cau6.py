N = int(input("Nhập số lượng phần tử N: "))
lst = []

print("Nhập các số (không trùng nhau):")
while len(lst) < N:
    x = int(input(f"Nhập số thứ {len(lst)+1}: "))
    if x not in lst:
        lst.append(x)
    else:
        print("Số này đã có rồi! Nhập lại.")

print("Danh sách bạn đã nhập là:")
print(lst)