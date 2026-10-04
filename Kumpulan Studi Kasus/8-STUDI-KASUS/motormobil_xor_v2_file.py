bawa_motor = False
bawa_mobil = True

bisa_berangkat = bawa_motor ^ bawa_mobil

if bisa_berangkat:
    print("Mahasiswa SIAP berangkat ke kampus")
else:
    print("Batal berangkat: Kendaraan tidak valid")