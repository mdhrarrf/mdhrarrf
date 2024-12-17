# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Pola Makan

def kategori_pola_makan(pola_makan):
    if pola_makan == "sehat":
        return "Kesehatan Jantung: Sangat Baik"
    elif pola_makan == "cukup sehat":
        return "Kesehatan Jantung: Baik"
    elif pola_makan == "kurang sehat":
        return "Kesehatan Jantung: Cukup"
    else:
        return "Kesehatan Jantung: Buruk"

# Judul Program
print("\033[1;34mProgram 34: Menentukan Kategori Kesehatan Jantung Berdasarkan Pola Makan\033[0m")
# Input dari pengguna
pola_makan_input = input("Masukkan pola makan Anda (sehat/cukup sehat/kurang sehat): ").lower()
print(kategori_pola_makan(pola_makan_input))