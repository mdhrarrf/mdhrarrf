# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function Sum

def total_angka(angka):
    return sum(angka)

# Judul Program
print("\033[1;34mProgram 3: Menggunakan Fungsi sum()\033[0m")
angka_input = list(map(int, input("Masukkan angka-angka (pisahkan dengan spasi): ").split()))
print("Total dari angka-angka tersebut adalah:", total_angka(angka_input))