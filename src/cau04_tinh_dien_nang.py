cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# DU DOAN 1: 
# dien_nang_kwh se la 0.375 (thuoc kieu <class 'float'>)
# chi_phi se la 1125.0 (thuoc kieu <class 'float'>)
print("Dien nang (kWh):", dien_nang_kwh, type(dien_nang_kwh))
print("Chi phi (VND):", chi_phi, type(chi_phi))


# Thay so_phut = 60 chay lai va so sanh
so_phut = 60
dien_nang_kwh_2 = cong_suat_w * so_phut / 60 / 1000
chi_phi_2 = dien_nang_kwh_2 * don_gia_kwh

# DU DOAN 2: 
# dien_nang_kwh_2 se la 0.25
# chi_phi_2 se la 750.0
print("Sau khi doi so phut = 60:")
print("Dien nang:", dien_nang_kwh_2)
print("Chi phi:", chi_phi_2)