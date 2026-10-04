member_premium = True
belanja_besar = True

dapat_cashback = member_premium and belanja_besar
gratis_ongkir = member_premium and belanja_besar

if dapat_cashback:
    print("Pelanggan MENDAPAT cashback")
else:
    print("Pelanggan TIDAK MENDAPAT cashback")

if gratis_ongkir:
    print("Pelanggan MENDAPAT gratis ongkir")
else:
    print("Pelanggan tidak mendapat gratis ongkir")