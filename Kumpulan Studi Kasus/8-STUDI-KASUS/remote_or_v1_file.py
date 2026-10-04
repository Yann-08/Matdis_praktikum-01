pakai_remote_tv = True
pakai_aplikasi_hp = False

# Model logika
tv_merespons = pakai_remote_tv or pakai_aplikasi_hp

# Output hasil kendali TV
if tv_merespons:
    print("Smart TV MENYALA / Merespons perintah")
else:
    print("Smart TV TIDAK MERESPONS (Tidak ada input)")