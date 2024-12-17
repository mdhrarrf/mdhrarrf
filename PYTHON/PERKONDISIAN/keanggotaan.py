# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Status Keanggotaan

def status_keanggotaan(umur):
    if umur < 12:
        return "Keanggotaan: Anak-anak"
    elif 12 <= umur < 18:
        return "Keanggotaan: Remaja"
    elif 18 <= umur < 60:
        return "Keanggotaan: Dewasa"
    else:
        return "Keanggotaan: Lansia"

# Judul Program
print("\033[1;34mProgram 10: Menentukan Status Keanggotaan Berdasarkan Umur\033[0m")
# Input dari pengguna
umur_input = int(input("Masukkan umur Anda: "))
print(status_keanggotaan(umur_input))