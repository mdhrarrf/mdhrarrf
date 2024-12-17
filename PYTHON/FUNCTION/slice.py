# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function Slice

def ambil_slice(daftar, start, end):
    return daftar[start:end]

# Judul Program
print("\033[1;34mProgram 14: Menggunakan Fungsi slice()\033[0m")
daftar_input = input("Masukkan elemen daftar (pisahkan dengan spasi): ").split()
start_input = int(input("Masukkan index awal: "))
end_input = int(input("Masukkan index akhir: "))
print("Slice dari daftar:", ambil_slice(daftar_input, start_input, end_input))