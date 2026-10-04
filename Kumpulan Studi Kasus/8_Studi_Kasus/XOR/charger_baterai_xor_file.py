batas_daya_80 = True
isi_penuh_100 = True

profil_daya_aman = batas_daya_80 ^ isi_penuh_100

if profil_daya_aman:
    print("Profil pengisian daya BERHASIL diterapkan")
else:
    print("Konflik pengaturan: Tidak bisa menerapkan dua batas pengisian sekaligus")