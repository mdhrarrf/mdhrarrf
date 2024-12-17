# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Usia Hewan

def kategori_usia_hewan(usia):
    if usia < 1:
        return "Kategori: Anak"
    elif 1 <= usia < 7:
        return "Kategori: Dewasa"
    else:
        return "Kategori: Lansia"

# Judul Program
print("\033[1;34mProgram 20: Menentukan Kategori Usia Hewan Peliharaan\033[0m")
# Input dari pengguna
usia_input = float(input("Masukkan usia hewan peliharaan Anda (dalam tahun): "))
print(kategori_usia_hewan(usia_input))