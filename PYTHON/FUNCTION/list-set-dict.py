# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function List, Set, & Dict

def konversi_koleksi(data):
    return list(data), set(data), dict.fromkeys(data, 0)

# Judul Program
print("\033[1;34mProgram 11: Menggunakan Fungsi list(), set(), dan dict()\033[0m")
data_input = input("Masukkan elemen (pisahkan dengan spasi): ").split()
list_output, set_output, dict_output = konversi_koleksi(data_input)
print("List:", list_output)
print("Set:", set_output)
print("Dictionary:", dict_output)