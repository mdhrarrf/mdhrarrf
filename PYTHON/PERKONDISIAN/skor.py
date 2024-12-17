# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Skor

def kategori_skor(skor):
    if skor >= 90:
        return "Kategori: Sangat Baik"
    elif skor >= 75:
        return "Kategori: Baik"
    elif skor >= 60:
        return "Kategori: Cukup"
    else:
        return "Kategori: Kurang"

# Judul Program
print("\033[1;34mProgram 11: Menentukan Kategori Skor Olahraga\033[0m")
# Input dari pengguna
skor_input = float(input("Masukkan skor olahraga Anda: "))
print(kategori_skor(skor_input))