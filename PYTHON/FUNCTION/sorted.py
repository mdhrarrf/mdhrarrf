# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function Sorted

def urutkan_angka(angka):
    return sorted(angka)

# Judul Program
print("\033[1;34mProgram 4: Menggunakan Fungsi sorted()\033[0m")
angka_input = list(map(int, input("Masukkan angka-angka (pisahkan dengan spasi): ").split()))
print("Angka-angka yang diurutkan adalah:", urutkan_angka(angka_input))