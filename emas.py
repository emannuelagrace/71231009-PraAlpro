#harga emas saat Gerard membeli
hbe = 650000

#harga emas terbaru
heb = 685000

#berat emas
be = 25
#berat emas baru Gerard
beg = 15

#keuntungan
untung = (heb*be) - hbe

#presentase keuntungan
persen_untung = untung * 100/hbe

#Gerard membeli emas 25g dengan harga Rp.650000
print('Keuntungan: Rp.', untung)
print('Presentase keuntungan:',persen_untung)

#harga berat emas baru
beb = beg*hbe

#total harga emas lama dan terbaru gerard
total_harga = (be*heb)+beb

harga_emas_skrg = 715000
emas_gerskrg = 40
ttl_emas = harga_emas_skrg*emas_gerskrg

untung1 = ttl_emas - total_harga
presentase_untung = untung1 * 100/beb

print("Keuntungan baru: Rp. ", untung1)
print('Presentase keuntungan baru: ', presentase_untung)