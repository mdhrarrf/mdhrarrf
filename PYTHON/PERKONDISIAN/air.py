# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Kualitas Air

def kategori_kualitas_air(pH):
    if pH < 6.5:
        return "Kualitas Air: Asam"
    elif 6.5 <= pH <= 8.5:
        return "Kualitas Air: Normal"
    else:
        return "Kualitas Air: Basa"

# Judul Program
print("\033[1;34mProgram 17: Menentukan Kategori Kualitas Air Berdasarkan pH\033[0m")
# Input dari pengguna
pH_input = float(input("Masukkan nilai pH air: "))
print(kategori_kualitas_air(pH_input))