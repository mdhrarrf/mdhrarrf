# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function Reduce

from functools import reduce

def jumlahkan(angka):
    return reduce(lambda x, y: x + y, angka)

# Judul Program
print("\033[1;34mProgram 19: Menggunakan Fungsi reduce()\033[0m")
angka_input = list(map(int, input("Masukkan angka-angka (pisahkan dengan spasi): ").split()))
total = jumlahkan(angka_input)
print("Jumlah total dari angka-angka tersebut adalah:", total)