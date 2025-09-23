import os

def LayTenFileDuoi(path):
    return os.path.basename(path)
def LayTenFileKhongDuoi(path):
    return os.path.splitext(os.path.basename(path))[0]
duong_dan = input("Nhập vào đường dẫn file nhạc: ")
print("Tên file có đuôi:", LayTenFileDuoi(duong_dan))       # muabui.mp3
print("Tên file không đuôi:", LayTenFileKhongDuoi(duong_dan))  # muabui
