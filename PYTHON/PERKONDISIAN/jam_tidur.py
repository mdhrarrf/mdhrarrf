# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Kualitas Tidur

def kategori_kualitas_tidur(jam_tidur):
    if jam_tidur < 5:
        return "Kualitas Tidur: Buruk"
    elif 5 <= jam_tidur < 7:
        return "Kualitas Tidur: Cukup"
    elif 7 <= jam_tidur <= 9:
        return "Kualitas Tidur: Baik"
    else:
        return "Kualitas Tidur: Sangat Baik"

# Judul Program
print("\033[1;34mProgram 25: Menentukan Kategori Kualitas Tidur Berdasarkan Jam Tidur\033[0m")
# Input dari pengguna
jam_tidur_input = float(input("Masukkan jumlah jam tidur Anda: "))
print(kategori_kualitas_tidur(jam_tidur_input))