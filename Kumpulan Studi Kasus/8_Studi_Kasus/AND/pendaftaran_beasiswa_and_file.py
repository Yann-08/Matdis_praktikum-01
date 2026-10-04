status_mahasiswa = True
ipk_memenuhi = True
berkas_lengkap = True
rekomendasi_dosen = True
prestasi_lomba = True	

lolos_utama = status_mahasiswa and ipk_memenuhi and berkas_lengkap

jalur_khusus = rekomendasi_dosen and prestasi_lomba

if lolos_utama:
    print("Peserta LOLOS seleksi beasiswa utama")
else:
    print("Peserta TIDAK LOLOS seleksi beasiswa utama")

if jalur_khusus:
    print("Peserta berhak mengikuti seleksi JALUR KHUSUS")
else:
    print("Peserta tidak masuk dalam kriteria jalur khusus")