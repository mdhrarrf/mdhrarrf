# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Kualitas Hidup

def kategori_kualitas_hidup(skor):
    if skor < 25:
        return "Kualitas Hidup: Sangat Buruk"
    elif 25 <= skor < 50:
        return "Kualitas Hidup: Buruk"
    elif 50 <= skor < 75:
        return "Kualitas Hidup: Cukup"
    else:
        return "Kualitas Hidup: Baik"

# Judul Program
print("\033[1;34mProgram 28: Menentukan Kategori Kualitas Hidup Berdasarkan Skor Kuesioner\033[0m")
# Input dari pengguna
skor_input = int(input("Masukkan skor kualitas hidup (0-100): "))
print(kategori_kualitas_hidup(skor_input))