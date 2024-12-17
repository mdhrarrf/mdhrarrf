# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Kualitas Udara

def kategori_kualitas_udara(indeks_polusi):
    if indeks_polusi <= 50:
        return "Kualitas Udara: Baik"
    elif 51 <= indeks_polusi <= 100:
        return "Kualitas Udara: Sedang"
    elif 101 <= indeks_polusi <= 150:
        return "Kualitas Udara: Tidak Sehat untuk Kelompok Sensitif"
    elif 151 <= indeks_polusi <= 200:
        return "Kualitas Udara: Tidak Sehat"
    else:
        return "Kualitas Udara: Sangat Tidak Sehat"

# Judul Program
print("\033[1;34mProgram 23: Menentukan Kategori Kualitas Udara Berdasarkan Indeks Polusi\033[0m")
# Input dari pengguna
indeks_polusi_input = float(input("Masukkan indeks polusi udara: "))
print(kategori_kualitas_udara(indeks_polusi_input))