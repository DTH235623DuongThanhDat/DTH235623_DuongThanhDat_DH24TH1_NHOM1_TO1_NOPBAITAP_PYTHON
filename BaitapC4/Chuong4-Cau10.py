import time

def ve_hinh1():
    # Danh sách tọa độ (hàng, cột) của các dấu *
    toa_do = [
        (3, 0), (4, 0), (5, 0), (6, 0),  #4 dấu * ở cột đầu
        (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), #dấu * ở hàng giữa
        (0, 3), (1, 3), (2, 3), (3, 3), (3, 6), 
        (1, 4), (2, 4), (2, 5), (4, 1), (4, 2), (5, 1) #dấu * đường chéo
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


def ve_hinh2():
    # Danh sách tọa độ (hàng, cột) của các dấu *
    toa_do = [
        (3, 0), (4, 0), (5, 0), (6, 0),  #4 dấu * ở cột đầu
        (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), #dấu * ở hàng giữa
        (0, 3), (1, 3), (2, 3), (3, 3), (3, 6), 
        (1, 4), (2, 5), (4, 2), (5, 1) #dấu * đường chéo
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

def ve_hinh3():
    # Danh sách tọa độ (hàng, cột) của các dấu *
    toa_do = [
        (0, 4), (0, 5), (0, 6),#Ngang trên 
        (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),  # Hàng dọc
        (1, 4), (1, 5), (2, 4), (4, 2), (4, 3), (5, 1), (5, 2), # Đường chéo ngang
        (6, 0),(6, 1), (6, 2), #Ngang dưới
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

def ve_hinh4():
    # Danh sách tọa độ (hàng, cột) của các dấu *
    toa_do = [
        (0, 4), (0, 5), (0, 6),#Ngang trên 
        (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),  # Hàng dọc
        (1, 5), (2, 4), (4, 2), (4, 3), (5, 1), # Đường chéo ngang
        (6, 0),(6, 1), (6, 2), #Ngang dưới
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


for ve in [ve_hinh1, ve_hinh2, ve_hinh3, ve_hinh4]:
    ve()
    time.sleep(5)   # chờ 5 giây trước khi in hình tiếp theo
    print("\n" + "-"*20 + "\n")  # phân cách giữa các hình