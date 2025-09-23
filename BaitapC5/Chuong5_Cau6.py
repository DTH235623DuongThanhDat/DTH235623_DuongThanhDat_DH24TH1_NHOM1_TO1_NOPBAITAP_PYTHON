import re

def NegativeNumberInStrings(str):
    # Tìm tất cả các số nguyên âm trong chuỗi bằng biểu thức chính quy
    so_am = re.findall(r'-\d+', str)
    
    # Chuyển các số từ chuỗi sang số nguyên
    so_am_int = [int(x) for x in so_am]
    
    # Xuất kết quả
    print("Các số nguyên âm trong chuỗi là:", so_am_int)
chuoi = "abc-5xyz-12k9l--p"
NegativeNumberInStrings(chuoi)
