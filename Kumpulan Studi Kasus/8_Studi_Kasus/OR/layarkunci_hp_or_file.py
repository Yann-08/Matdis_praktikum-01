sidik_jari_cocok = True
wajah_dikenali = True

hp_terbuka = sidik_jari_cocok or wajah_dikenali

if hp_terbuka:
    print("Kunci layar TERBUKA / Mengakses menu utama")
else:
    print("Akses DITOLAK (Autentikasi gagal)")