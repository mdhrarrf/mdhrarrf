# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function Filter 

def genap(angka):
    return angka % 2 == 0

# Judul Program
print("\033[1;34mProgram 6: Menggunakan Fungsi filter()\033[0m")
angka_input = list(map(int, input("Masukkan angka-angka (pisahkan dengan spasi): ").split()))
angka_genap = list(filter(genap, angka_input))
print("Angka genap dari input adalah:", angka_genap)