bayar_tunai = True
bayar_kartu = True

pembayaran_valid = bayar_tunai ^ bayar_kartu

if pembayaran_valid:
    print("Pembayaran berhasil diproses.")
else:
    print("Transaksi Gagal: Silakan pilih HANYA satu metode pembayaran.")