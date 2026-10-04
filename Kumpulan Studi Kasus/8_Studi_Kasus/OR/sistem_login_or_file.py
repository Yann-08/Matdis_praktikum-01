login_pakai_email = True
login_pakai_google = True

berhasil_masuk = login_pakai_email or login_pakai_google

if berhasil_masuk:
    print("Akses DITERIMA / Berhasil masuk ke beranda aplikasi")
else:
    print("Akses DITOLAK (Tidak ada metode login yang valid)")