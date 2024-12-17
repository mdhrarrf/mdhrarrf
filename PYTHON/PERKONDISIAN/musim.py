# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Musim Bulan

def musim_bulan(bulan):
    if bulan in [12, 1, 2]:
        return "Musim: Musim Dingin"
    elif bulan in [3, 4, 5]:
        return "Musim: Musim Semi"
    elif bulan in [6, 7, 8]:
        return "Musim: Musim Panas"
    elif bulan in [9, 10, 11]:
        return "Musim: Musim Gugur"
    else:
        return "Input tidak valid. Harap masukkan angka antara 1 dan 12."

# Judul Program
print("\033[1;34mProgram 5: Menentukan Musim Berdasarkan Bulan\033[0m")
# Input dari pengguna
bulan_input = int(input("Masukkan bulan (1-12): "))
print(musim_bulan(bulan_input))
