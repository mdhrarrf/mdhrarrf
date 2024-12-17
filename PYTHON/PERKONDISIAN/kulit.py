# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Kesehatan Kulit

def kategori_kesehatan_kulit(frekuensi):
    if frekuensi < 1:
        return "Kesehatan Kulit: Buruk"
    elif 1 <= frekuensi < 3:
        return "Kesehatan Kulit: Cukup"
    elif 3 <= frekuensi < 5:
        return "Kesehatan Kulit: Baik"
    else:
        return "Kesehatan Kulit: Sangat Baik"

# Judul Program
print("\033[1;34mProgram 30: Menentukan Kategori Kesehatan Kulit Berdasarkan Frekuensi Perawatan\033[0m")
# Input dari pengguna
frekuensi_input = int(input("Masukkan frekuensi perawatan kulit per minggu: "))
print(kategori_kesehatan_kulit(frekuensi_input))