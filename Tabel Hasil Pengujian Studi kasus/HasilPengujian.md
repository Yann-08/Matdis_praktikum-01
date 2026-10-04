# Tabel Hasil Pengujian (Truth Table)

Folder ini berisi rekapitulasi hasil pengujian dari setiap operator logika Boolean yang diterapkan pada studi kasus di repository ini. Pengujian dilakukan dengan memasukkan kombinasi kondisi `True` (Benar) dan `False` (Salah).

---

## 1. Pengujian Logika `AND`
**Studi Kasus yang relevan:** Diskon Belanja (`diskon_belanja_and_file.py`), Pendaftaran Beasiswa (`pendaftaran_beasiswa_and_file.py`)

Logika `AND` hanya akan menghasilkan nilai **True** jika **semua** kondisi bernilai True.

| Skenario | Kondisi 1 | Kondisi 2 | Hasil Akhir (`AND`) | Kesimpulan |
| :---: | :---: | :---: | :---: | :--- |
| 1 | `True` | `True` | **`True`** | Program Berhasil / Syarat Terpenuhi |
| 2 | `True` | `False` | **`False`** | Program Gagal / Syarat Tidak Terpenuhi |
| 3 | `False` | `True` | **`False`** | Program Gagal / Syarat Tidak Terpenuhi |
| 4 | `False` | `False` | **`False`** | Program Gagal / Syarat Tidak Terpenuhi |

---

## 2. Pengujian Logika `OR`
**Studi Kasus yang relevan:** Kontrol Remote (`remote_or_v1_file.py`, `remote_or_v2_file.py`, `remote_or_v3_file.py`)

Logika `OR` akan menghasilkan nilai **True** jika **salah satu atau kedua** kondisi bernilai True.

| Skenario | Kondisi 1 | Kondisi 2 | Hasil Akhir (`OR`) | Kesimpulan |
| :---: | :---: | :---: | :---: | :--- |
| 1 | `True` | `True` | **`True`** | Program Berhasil / Aksi Berjalan |
| 2 | `True` | `False` | **`True`** | Program Berhasil / Aksi Berjalan |
| 3 | `False` | `True` | **`True`** | Program Berhasil / Aksi Berjalan |
| 4 | `False` | `False` | **`False`** | Program Gagal / Aksi Berhenti |

---

## 3. Pengujian Logika `XOR` (Exclusive OR)
**Studi Kasus yang relevan:** Simulasi Kendaraan (`motormobil_xor_file.py`, `motormobil_xor_v1_file.py`, `motormobil_xor_v2_file.py`)

Logika `XOR` akan menghasilkan nilai **True** HANYA JIKA **salah satu** kondisi bernilai True, tetapi tidak keduanya. (Jika keduanya True atau keduanya False, hasilnya False).

| Skenario | Kondisi 1 | Kondisi 2 | Hasil Akhir (`XOR`) | Kesimpulan |
| :---: | :---: | :---: | :---: | :--- |
| 1 | `True` | `True` | **`False`** | Bentrok / Kondisi Tidak Valid |
| 2 | `True` | `False` | **`True`** | Program Berhasil / Valid |
| 3 | `False` | `True` | **`True`** | Program Berhasil / Valid |
| 4 | `False` | `False` | **`False`** | Tidak Ada Input / Kondisi Tidak Valid |

---

*Catatan: Hasil di atas didapatkan dari pengujian langsung (running text) terhadap file Python yang ada pada direktori utama.*
