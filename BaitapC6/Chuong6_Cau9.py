def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập số phần tử
N = int(input("Nhập số phần tử của mảng: "))

# Nhập từng phần tử
M = []
for i in range(N):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    M.append(x)

# Dòng 1: Số lẻ
so_le = [x for x in M if x % 2 != 0]
print("\nCác số lẻ:", so_le)
print("Tổng cộng có", len(so_le), "số lẻ")

# Dòng 2: Số chẵn
so_chan = [x for x in M if x % 2 == 0]
print("\nCác số chẵn:", so_chan)
print("Tổng cộng có", len(so_chan), "số chẵn")

# Dòng 3: Số nguyên tố
so_nguyen_to = [x for x in M if la_nguyen_to(x)]
print("\nCác số nguyên tố:", so_nguyen_to)

# Dòng 4: Không phải số nguyên tố
khong_nt = [x for x in M if not la_nguyen_to(x)]
print("\nCác số không phải là số nguyên tố:", khong_nt)
