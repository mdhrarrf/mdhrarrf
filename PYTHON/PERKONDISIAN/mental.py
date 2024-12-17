# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Kesehatan Mental

def kategori_kesehatan_mental(skor):
    if skor < 20:
        return "Kesehatan Mental: Sangat Baik"
    elif 20 <= skor < 40:
        return "Kesehatan Mental: Baik"
    elif 40 <= skor < 60:
        return "Kesehatan Mental: Cukup"
    else:
        return "Kesehatan Mental: Buruk"

# Judul Program
print("\033[1;34mProgram 24: Menentukan Kategori Kesehatan Mental Berdasarkan Skor Kuesioner\033[0m")
# Input dari pengguna
skor_input = int(input("Masukkan skor kuesioner (0-100): "))
print(kategori_kesehatan_mental(skor_input))