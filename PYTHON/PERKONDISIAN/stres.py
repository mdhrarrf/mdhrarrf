# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Stres

def kategori_stres(frekuensi_stres):
    if frekuensi_stres < 1:
        return "Kesehatan Mental: Sangat Baik"
    elif 1 <= frekuensi_stres < 3:
        return "Kesehatan Mental: Baik"
    elif 3 <= frekuensi_stres < 5:
        return "Kesehatan Mental: Cukup"
    else:
        return "Kesehatan Mental: Buruk"

# Judul Program
print("\033[1;34mProgram 32: Menentukan Kategori Kesehatan Mental Berdasarkan Frekuensi Stres\033[0m")
# Input dari pengguna
frekuensi_stres_input = int(input("Masukkan frekuensi stres per minggu: "))
print(kategori_stres(frekuensi_stres_input))