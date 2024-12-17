# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Pekerjaan

def kategori_pekerjaan(gaji):
    if gaji < 3000000:
        return "Kategori: Pekerja Rendah"
    elif 3000000 <= gaji < 7000000:
        return "Kategori: Pekerja Menengah"
    else:
        return "Kategori: Pekerja Tinggi"

# Judul Program
print("\033[1;34mProgram 14: Menentukan Kategori Pekerjaan Berdasarkan Gaji\033[0m")
# Input dari pengguna
gaji_input = float(input("Masukkan gaji bulanan Anda: "))
print(kategori_pekerjaan(gaji_input))