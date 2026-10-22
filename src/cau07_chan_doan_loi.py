ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: "))  # Da sua: ep kieu str sang float
so_phut = int(input("Nhap so phut: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")
# Mo ta cac loi da phat hien:
# - Loi 1 (TypeError): Ham input() mac dinh tra ve kieu chuoi (str). Khong the dung toan tu nhan (*) truc tiep giua chuoi va so.
# - Cach khac phuc: Su dung ham float() de chuyen doi du lieu nhap vao cua cong_suat_w sang kieu so thuc truoc khi thuc hien tinh toan dien nang.