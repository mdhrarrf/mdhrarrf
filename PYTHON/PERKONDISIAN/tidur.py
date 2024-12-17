# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Kualitas Tidur

def kategori_kualitas_tidur_rata(jam_tidur_rata):
    if jam_tidur_rata < 6:
        return "Kualitas Tidur: Buruk"
    elif 6 <= jam_tidur_rata < 8:
        return "Kualitas Tidur: Cukup"
    elif 8 <= jam_tidur_rata <= 10:
        return "Kualitas Tidur: Baik"
    else:
        return "Kualitas Tidur: Sangat Baik"

# Judul Program
print("\033[1;34mProgram 31: Menentukan Kategori Kualitas Tidur Berdasarkan Jam Tidur Rata-rata\033[0m")
# Input dari pengguna
jam_tidur_rata_input = float(input("Masukkan jam tidur rata-rata Anda per malam: "))
print(kategori_kualitas_tidur_rata(jam_tidur_rata_input))