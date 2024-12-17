# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function Reversed

def balikkan_list(daftar):
    return list(reversed(daftar))

# Judul Program
print("\033[1;34mProgram 13: Menggunakan Fungsi reversed()\033[0m")
daftar_input = input("Masukkan elemen daftar (pisahkan dengan spasi): ").split()
print("Daftar yang dibalik:", balikkan_list(daftar_input))