# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori IMT

def kategori_imt(imt):
    if imt < 18.5:
        return "Kekurangan berat badan"
    elif 18.5 <= imt < 24.9:
        return "Berat badan normal"
    elif 25 <= imt < 29.9:
        return "Kelebihan berat badan"
    else:
        return "Obesitas"

# Judul Program
print("\033[1;34mProgram 22: Menentukan Kategori Kesehatan Berdasarkan Indeks Massa Tubuh (IMT)\033[0m")
# Input dari pengguna
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))
imt = berat / (tinggi ** 2)
print(kategori_imt(imt))