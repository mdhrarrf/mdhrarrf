# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Aktivitas Fisik

def kategori_aktivitas_fisik(jumlah_aktivitas):
    if jumlah_aktivitas < 1:
        return "Kesehatan Mental: Buruk"
    elif 1 <= jumlah_aktivitas < 3:
        return "Kesehatan Mental: Cukup"
    elif 3 <= jumlah_aktivitas < 5:
        return "Kesehatan Mental: Baik"
    else:
        return "Kesehatan Mental: Sangat Baik"

# Judul Program
print("\033[1;34mProgram 35: Menentukan Kategori Kesehatan Mental Berdasarkan Aktivitas Fisik\033[0m")
# Input dari pengguna
jumlah_aktivitas_input = int(input("Masukkan jumlah aktivitas fisik per minggu: "))
print(kategori_aktivitas_fisik(jumlah_aktivitas_input))