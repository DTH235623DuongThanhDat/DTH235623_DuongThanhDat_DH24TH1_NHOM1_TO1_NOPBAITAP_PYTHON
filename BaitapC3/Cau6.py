def doc_so(n):
	don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
	dac_biet = {1: "mốt", 4: "tư", 5: "lăm"}
	if n < 0 or n > 99:
		return "Chỉ nhập số có tối đa 2 chữ số (0-99)"
	if n == 0:
		return "không"
	if n < 10:
		return don_vi[n]
	chuc = n // 10
	dv = n % 10
	if chuc == 1:
		if dv == 0:
			return "mười"
		elif dv == 5:
			return "mười lăm"
		else:
			return f"mười {don_vi[dv]}"
	else:
		chuoi = f"{don_vi[chuc].capitalize()} mươi"
		if dv == 0:
			return chuoi
		if dv in dac_biet:
			return f"{chuoi} {dac_biet[dv]}"
		return f"{chuoi} {don_vi[dv]}"

try:
	n = int(input("Nhập số nguyên n (0-99): "))
	print(doc_so(n))
except ValueError:
	print("Vui lòng nhập số nguyên hợp lệ!")
