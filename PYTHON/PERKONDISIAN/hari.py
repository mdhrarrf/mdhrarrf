# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Nama Hari

def nama_hari(angka):
    if angka == 1:
        return "Senin"
    elif angka == 2:
        return "Selasa"
    elif angka == 3:
        return "Rabu"
    elif angka == 4:
        return "Kamis"
    elif angka == 5:
        return "Jumat"
    elif angka == 6:
        return "Sabtu"
    elif angka == 7:
        return "Minggu"
    else:
        return "Input tidak valid. Harap masukkan angka antara 1 dan 7."

# Judul Program
print("\033[1;34mProgram 4: Menentukan Hari dalam Angka\033[0m")
# Input dari pengguna
hari_input = int(input("Masukkan angka hari (1-7): "))
print(nama_hari(hari_input))