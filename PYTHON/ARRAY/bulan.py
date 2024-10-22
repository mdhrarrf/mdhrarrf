# Muhammad Haidar Almer Rafif
# 22/10/24
# Program Belajar Array (Bulan)

bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
print(bulan[2])
print(bulan[9])
bulan[7] = 'August'
bulan[0] = 'January'
bulan.append('Muharram')
i = 1
for data in bulan:
    print('Bulan',i, data)
    i = i+1
