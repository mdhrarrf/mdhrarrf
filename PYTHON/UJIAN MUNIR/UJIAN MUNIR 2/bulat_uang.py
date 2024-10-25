# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Membulatkan Uang

while True:
    def membulatkan_uang(jumlah):
        pecahan = [100, 50, 25]

        for nilai in pecahan:
            if jumlah >= nilai:
                return (jumlah // nilai) * nilai

        return 0

    jumlah_uang = int(input("\nMasukkan jumlah uang: "))
    hasil = membulatkan_uang(jumlah_uang)
    
    print(f"\nJumlah uang yang dibulatkan ke pecahan terdekat: {hasil}")