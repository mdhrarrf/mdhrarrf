# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Tekanan Darah

def kategori_tekanan_darah(tekanan_darah):
    if tekanan_darah < 90:
        return "Kategori: Hipotensi"
    elif 90 <= tekanan_darah <= 120:
        return "Kategori: Normal"
    elif 120 < tekanan_darah <= 140:
        return "Kategori: Pra-hipertensi"
    else:
        return "Kategori: Hipertensi"

# Judul Program
print("\033[1;34mProgram 18: Menentukan Kategori Kesehatan Berdasarkan Tekanan Darah\033[0m")
# Input dari pengguna
tekanan_darah_input = float(input("Masukkan tekanan darah Anda (mmHg): "))
print(kategori_tekanan_darah(tekanan_darah_input))