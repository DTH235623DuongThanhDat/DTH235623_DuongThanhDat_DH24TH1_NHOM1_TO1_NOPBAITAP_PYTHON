def ToiUuChuoiDanhTu(s):
    # Loại bỏ khoảng trắng đầu và cuối
    s = s.strip()
    
    # Tách chuỗi thành các từ, loại bỏ khoảng trắng dư thừa
    toiuu = s.split()
    
    # Viết hoa chữ cái đầu mỗi từ
    toiuu = [word.capitalize() for word in toiuu]
    
    # Ghép lại thành chuỗi với khoảng trắng đúng chuẩn
    ket_qua = ' '.join(toiuu)
    
    return ket_qua

# Nhập chuỗi từ người dùng
chuoi = input("Nhập vào chuỗi danh từ: ")

# Gọi hàm xử lý
ket_qua = ToiUuChuoiDanhTu(chuoi)

# Xuất kết quả
print("Chuỗi sau khi tối ưu:", ket_qua)
