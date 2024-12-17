# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Frekuensi Olahraga

def kategori_frekuensi_olahraga(frekuensi):
    if frekuensi < 1:
        return "Kesehatan Fisik: Buruk"
    elif 1 <= frekuensi < 3:
        return "Kesehatan Fisik: Cukup"
    elif 3 <= frekuensi < 5:
        return "Kesehatan Fisik: Baik"
    else:
        return "Kesehatan Fisik: Sangat Baik"

# Judul Program
print("\033[1;34mProgram 38: Menentukan Kategori Kesehatan Fisik Berdasarkan Frekuensi Olahraga\033[0m")
# Input dari pengguna
frekuensi_olahraga_input = int(input("Masukkan frekuensi olahraga per minggu: "))
print(kategori_frekuensi_olahraga(frekuensi_olahraga_input))