# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Genap Ganjil

def genap_ganjil(angka):
    if angka % 2 == 0:
        return "Bilangan Genap"
    else:
        return "Bilangan Ganjil"

# Judul Program
print("\033[1;34mProgram 6: Menentukan Bilangan Genap atau Ganjil\033[0m")
# Input dari pengguna
angka_input = int(input("Masukkan sebuah angka: "))
print(genap_ganjil(angka_input))