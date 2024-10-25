# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Mengkonversi Hari-Bulan-tahun

TAHUN_HARI = 365
BULAN_HARI = 30
hari = int(input('Masukan Hari: '))
tahun = int(hari / TAHUN_HARI)
hari = hari % TAHUN_HARI
bulan = int(hari / BULAN_HARI)
hari = hari % BULAN_HARI

print(tahun, ' tahun ', bulan, ' bulan ', hari, ' hari ')