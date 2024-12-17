# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function Split

def pisahkan_string(teks):
    return teks.split()

# Judul Program
print("\033[1;34mProgram 18: Menggunakan Fungsi split()\033[0m")
teks_input = input("Masukkan sebuah kalimat: ")
print("Kata-kata dalam kalimat tersebut:", pisahkan_string(teks_input))