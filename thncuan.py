uang = 200000000
mincuan = 400000000
bunga = 0.1
n = 1
t = 0

while uang < mincuan:
    uang = uang*(1+bunga/n)
    t += 1
print('Butuh: ', t, "tahun")