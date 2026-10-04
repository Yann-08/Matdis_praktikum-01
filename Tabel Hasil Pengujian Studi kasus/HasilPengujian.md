# TABEL PENGUJIAN

Tabel pengujian digunakan untuk menguji setiap studi kasus dengan beberapa kombinasi kondisi `True` dan `False`.

## 1. PENGUJIAN LOGIKA - `AND`

**Studi Kasus 1: Pendaftaran Beasiswa**
| status_mahasiswa | ipk_memenuhi | berkas_lengkap | rekomendasi_dosen | prestasi_lomba | Hasil Beasiswa Utama | Hasil Jalur Khusus |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| True | True | True | False | False | Peserta LOLOS seleksi beasiswa utama | Peserta tidak masuk dalam kriteria jalur khusus |
| True | True | True | True | True | Peserta LOLOS seleksi beasiswa utama | Peserta berhak mengikuti seleksi JALUR KHUSUS |
| False | True | True | True | True | Peserta TIDAK LOLOS seleksi beasiswa utama | Peserta berhak mengikuti seleksi JALUR KHUSUS |
| True | False | True | False | True | Peserta TIDAK LOLOS seleksi beasiswa utama | Peserta tidak masuk dalam kriteria jalur khusus |
| False | False | False | False | False | Peserta TIDAK LOLOS seleksi beasiswa utama | Peserta tidak masuk dalam kriteria jalur khusus |

**Studi Kasus 2: Diskon Belanja**
| member_premium | belanja_besar | Hasil |
| :--- | :--- | :--- |
| True | True | Pelanggan MENDAPAT cashback |
| False | True | Pelanggan TIDAK MENDAPAT cashback |
| True | False | Pelanggan TIDAK MENDAPAT cashback |
| False | False | Pelanggan TIDAK MENDAPAT cashback |

## 2. PENGUJIAN LOGIKA - `OR`

**Studi Kasus 3: Sistem Login**
| login_pakai_email | login_pakai_google | Hasil |
| :--- | :--- | :--- |
| True | True | Akses DITERIMA / Berhasil masuk ke beranda aplikasi |
| False | True | Akses DITERIMA / Berhasil masuk ke beranda aplikasi |
| True | False | Akses DITERIMA / Berhasil masuk ke beranda aplikasi |
| False | False | Akses DITOLAK (Tidak ada metode login yang valid) |

**Studi Kasus 4: Smart tv**
| pakai_remote_tv | pakai_aplikasi_hp | Hasil |
| :--- | :--- | :--- |
| True | True | Smart TV MENYALA / Merespons perintah |
| False | True | Smart TV MENYALA / Merespons perintah |
| True | False | Smart TV MENYALA / Merespons perintah |
| False | False | Smart TV TIDAK MERESPONS (Tidak ada input) |

**Studi Kasus 5: Layar Kunci Handphone**
| sidik_jari_cocok | wajah_dikenali | Hasil |
| :--- | :--- | :--- |
| True | True | Kunci layar TERBUKA / Mengakses menu utama |
| False | True | Kunci layar TERBUKA / Mengakses menu utama |
| True | False | Kunci layar TERBUKA / Mengakses menu utama |
| False | False | Akses DITOLAK (Autentikasi gagal) |

## 3. PENGUJIAN LOGIKA - `XOR`

**Studi Kasus 6: Kendaraan**
| bawa_motor | bawa_mobil | Hasil |
| :--- | :--- | :--- |
| True | True | Batal berangkat: Kendaraan tidak valid |
| False | True | Mahasiswa SIAP berangkat ke kampus |
| True | False | Mahasiswa SIAP berangkat ke kampus |
| False | False | Batal berangkat: Kendaraan tidak valid |

**Studi Kasus 7: Charger Baterai**
| batas_daya_80 | isi_penuh_100 | Hasil |
| :--- | :--- | :--- |
| True | True | Konflik pengaturan: Tidak bisa menerapkan dua batas pengisian sekaligus |
| False | True | Profil pengisian daya BERHASIL diterapkan |
| True | False | Profil pengisian daya BERHASIL diterapkan |
| False | False | Konflik pengaturan: Tidak bisa menerapkan dua batas pengisian sekaligus |

**Studi Kasus 8: Metode Pembayaran**
| bayar_tunai | bayar_kartu | Hasil |
| :--- | :--- | :--- |
| True | True | Transaksi Gagal: Silakan pilih HANYA satu metode pembayaran. |
| False | True | Pembayaran berhasil diproses. |
| True | False | Pembayaran berhasil diproses. |
| False | False | Transaksi Gagal: Silakan pilih HANYA satu metode pembayaran. |
