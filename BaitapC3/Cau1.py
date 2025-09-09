print ("Chương trình kiểm tra năm nhuần")
yeah = int(input("Nhập năm cần kiểm tra: "))
if (yeah % 4 == 0 and yeah % 100 != 0) or (yeah % 400 == 0):  
    print("Năm ", yeah, "là năm nhuận")
else:
    print("Năm ", yeah, "không phải là năm nhuận")