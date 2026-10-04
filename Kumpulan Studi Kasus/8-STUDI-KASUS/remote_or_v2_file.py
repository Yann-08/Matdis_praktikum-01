pakai_remote_tv = False
pakai_aplikasi_hp = False

tv_merespons = pakai_remote_tv or pakai_aplikasi_hp

if tv_merespons:
    print("Smart TV MENYALA / Merespons perintah")
else:
    print("Smart TV TIDAK MERESPONS (Tidak ada input)")