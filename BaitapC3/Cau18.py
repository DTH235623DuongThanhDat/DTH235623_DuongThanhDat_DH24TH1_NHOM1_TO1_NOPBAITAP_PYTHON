
#Hình Tam Giác Đối
def ve_hinh():
    # Danh sách tọa độ (hàng, cột) của các dấu *
    toa_do = [
        (0, 0), (1, 0), (2, 0), (3, 0),  #4 dấu * ở cột đầu
        (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), #dấu * ở hàng giữa
        (3, 6), (4, 6), (5, 6), (6, 6), #4 dấu * ở cột cuối
        (1, 1), (2, 2), (4, 4), (5, 5), (6, 6) #dấu * đường chéo
    ]

    # Xác định kích thước lưới
    max_hang = max(y for y, x in toa_do)
    max_cot = max(x for y, x in toa_do)

    # Duyệt qua từng dòng để in
    for i in range(max_hang + 1):
        for j in range(max_cot + 1):
            if (i, j) in toa_do:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Gọi hàm để in hình
ve_hinh()



#Hinh Vuông
n=4
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

      
n = 4 # Chiều cao của tam giác

# Dùng vòng lặp để vẽ tam giác vuông có góc vuông ở dưới bên phải
for i in range(1, n + 1):  # Dòng từ 1 đến n
    for j in range(n - i):  # In khoảng trắng để tạo khoảng cách
        print(' ', end='')  # In dấu cách trước dấu sao
    for k in range(i):  # In dấu sao
        print('*', end='')  # In dấu sao
    print()  # In xuống dòng sau mỗi dòng sao