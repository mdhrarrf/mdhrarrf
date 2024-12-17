# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function Join

def gabungkan_string(teks):
    return ", ".join(teks)

# Judul Program
print("\033[1;34mProgram 17: Menggunakan Fungsi join()\033[0m")
teks_input = input("Masukkan beberapa kata (pisahkan dengan spasi): ").split()
print("Gabungan string:", gabungkan_string(teks_input))