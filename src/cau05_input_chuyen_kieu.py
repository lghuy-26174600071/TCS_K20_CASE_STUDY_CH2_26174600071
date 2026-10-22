ma_may = input("Nhap ma may: ")
cong_suat_w = input("Nhap cong suat W: ")
so_phut = input("Nhap so phut: ")
don_gia_kwh = input("Nhap don gia/kWh: ")

# Chuyen doi kieu du lieu
cong_suat_w = float(cong_suat_w)
so_phut = int(so_phut)
don_gia_kwh = float(don_gia_kwh)

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Dien nang sau chuyen kieu:", dien_nang_kwh)
print("Chi phi sau chuyen kieu:", chi_phi)