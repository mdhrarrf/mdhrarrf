# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Kesehatan Gigi

def kategori_kesehatan_gigi(frekuensi):
    if frekuensi < 1:
        return "Kesehatan Gigi: Buruk"
    elif 1 <= frekuensi < 2:
        return "Kesehatan Gigi: Cukup"
    elif 2 <= frekuensi < 3:
        return "Kesehatan Gigi: Baik"
    else:
        return "Kesehatan Gigi: Sangat Baik"

# Judul Program
print("\033[1;34mProgram 27: Menentukan Kategori Kesehatan Gigi Berdasarkan Frekuensi Sikat Gigi\033[0m")
# Input dari pengguna
frekuensi_input = int(input("Masukkan frekuensi sikat gigi per hari: "))
print(kategori_kesehatan_gigi(frekuensi_input))