# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function String, Integer, & Float

def konversi_tipe(angka):
    return str(angka), int(angka), float(angka)

# Judul Program
print("\033[1;34mProgram 9: Menggunakan Fungsi str(), int(), dan float()\033[0m")
angka_input = input("Masukkan sebuah angka: ")
string_output, int_output, float_output = konversi_tipe(angka_input)
print("String:", string_output)
print("Integer:", int_output)
print("Float:", float_output)