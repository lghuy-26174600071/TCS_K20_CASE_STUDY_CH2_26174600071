from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))
#Bo sung tinh khoang thoi gian
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau

print("Thoi luong:", thoi_luong)
print("Kieu thoi luong:", type(thoi_luong))
#Du doan ket qua cua phep tru truoc khi chay
#Khoang thoi gian chenh lech giua 15:05 va 13:15 la 1 gio 50 phut.
#Ket qua in ra man hinh se co dinh dang timedelta la: 1:50:00
#Giai thich su khac nhau:
#datetime: Kieu du lieu moc thoi gian.
#str: Chuoi van ban bieu dien thoi gian sau khi dinh dang.
#timedelta: Khoang thoi gian (chenh lech giua 2 moc datetime).
