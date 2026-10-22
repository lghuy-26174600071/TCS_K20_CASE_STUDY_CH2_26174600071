tong_phut = 135
cong_suat_w = 250

# Dung // va % de tinh so gio tron ven va so phut con lai
so_gio = tong_phut // 60
so_phut_du = tong_phut % 60
print(f"So gio: {so_gio}, So phut: {so_phut_du}")

su_dung_lau = tong_phut > 60
print("Su dung tren 60 phut:", su_dung_lau)

du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Dieu kien hop le:", du_lieu_hop_le)

# Kiem chung bieu thuc
print(100 + 20 * 3) # Ket qua: 160 (Nhan truoc cong sau)
print((100 + 20) * 3) # Ket qua: 360 (Thuc hien trong ngoac truoc)