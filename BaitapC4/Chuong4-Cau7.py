# Tính và xuất độ dài đoạn AB với tọa độ nhập từ bàn phím
import math

x1 = float(input("Nhập hoành độ điểm A (x1): "))
y1 = float(input("Nhập tung độ điểm A (y1): "))
x2 = float(input("Nhập hoành độ điểm B (x2): "))
y2 = float(input("Nhập tung độ điểm B (y2): "))

do_dai_AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Độ dài đoạn AB là: ",do_dai_AB)
