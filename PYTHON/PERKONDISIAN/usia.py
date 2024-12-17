# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Usia

def kategori_usia(usia):
    if usia < 13:
        return "Anda adalah seorang anak."
    elif 13 <= usia < 20:
        return "Anda adalah seorang remaja."
    elif 20 <= usia < 65:
        return "Anda adalah seorang dewasa."
    else:
        return "Anda adalah seorang lansia."

# Judul Program
print("\033[1;34mProgram 1: Menentukan Kategori Usia\033[0m")
# Input dari pengguna
usia_input = int(input("Masukkan usia Anda: "))
print(kategori_usia(usia_input))
