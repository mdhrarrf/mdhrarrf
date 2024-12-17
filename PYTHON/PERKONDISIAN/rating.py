# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Film

def kategori_film(rating):
    if rating >= 8:
        return "Kategori: Sangat Bagus"
    elif rating >= 6:
        return "Kategori: Bagus"
    elif rating >= 4:
        return "Kategori: Cukup"
    else:
        return "Kategori: Buruk"

# Judul Program
print("\033[1;34mProgram 15: Menentukan Kategori Film Berdasarkan Rating\033[0m")
# Input dari pengguna
rating_input = float(input("Masukkan rating film (0-10): "))
print(kategori_film(rating_input))