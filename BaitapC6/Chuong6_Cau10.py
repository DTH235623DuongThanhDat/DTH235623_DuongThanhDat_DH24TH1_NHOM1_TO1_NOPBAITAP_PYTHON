# Hàm nhập ma trận từ bàn phím
def input_matrix(name):
    rows = int(input(f"Nhập số hàng của ma trận {name}: "))
    cols = int(input(f"Nhập số cột của ma trận {name}: "))
    print(f"Nhập các phần tử cho ma trận {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Hàng {i+1}: ").split()))
        while len(row) != cols:
            print(f"Vui lòng nhập đúng {cols} phần tử.")
            row = list(map(int, input(f"Hàng {i+1}: ").split()))
        matrix.append(row)
    return matrix

# Hàm cộng hai ma trận
def add_matrices(m1, m2):
    rows = len(m1)
    cols = len(m1[0])
    result = [[m1[i][j] + m2[i][j] for j in range(cols)] for i in range(rows)]
    return result

# Hàm hoán vị ma trận
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    return transposed

# Nhập ma trận A và B
A = input_matrix("A")
B = input_matrix("B")

# Kiểm tra kích thước trước khi cộng
if len(A) != len(B) or len(A[0]) != len(B[0]):
    print("Không thể cộng hai ma trận có kích thước khác nhau.")
else:
    C = add_matrices(A, B)
    print("\nMa trận A + B:")
    for row in C:
        print(row)

# Hoán vị ma trận A và B
print("\nMa trận hoán vị của A:")
for row in transpose_matrix(A):
    print(row)

print("\nMa trận hoán vị của B:")
for row in transpose_matrix(B):
    print(row)