# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function Enumerate

def tampilkan_daftar(daftar):
    for index, item in enumerate(daftar):
        print(f"Index {index}: {item}")

# Judul Program
print("\033[1;34mProgram 12: Menggunakan Fungsi enumerate()\033[0m")
daftar_input = input("Masukkan elemen daftar (pisahkan dengan spasi): ").split()
print("Daftar dengan index:")
tampilkan_daftar(daftar_input)