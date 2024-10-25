# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Mengkonversi Waktu

while True:
    HARI_DETIK = 60*60*24
    JAM_DETIK= 60*60

    detik = int(input('\nDetik : '))
    hari = int(detik/HARI_DETIK)
    detik = detik % HARI_DETIK
    jam = int(detik/JAM_DETIK)
    detik = detik % JAM_DETIK
    menit = int(detik/60)
    detik = detik % 60

    print(hari, ' hari ', ' detik ', ' adalah ', menit, ' menit', ' dan ',detik, ' detik ')