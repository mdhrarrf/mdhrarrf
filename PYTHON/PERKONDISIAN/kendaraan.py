# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Kendaraan

def kategori_kendaraan(jumlah_roda):
    if jumlah_roda == 2:
        return "Kendaraan: Sepeda/Motor"
    elif jumlah_roda == 4:
        return "Kendaraan: Mobil"
    elif jumlah_roda > 4:
        return "Kendaraan: Truk atau Bus"
    else:
        return "Input tidak valid. Jumlah roda tidak dapat kurang dari 2."

# Judul Program
print("\033[1;34mProgram 9: Menentukan Kategori Kendaraan Berdasarkan Jumlah Roda\033[0m")
# Input dari pengguna
roda_input = int(input("Masukkan jumlah roda kendaraan: "))
print(kategori_kendaraan(roda_input))