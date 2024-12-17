# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function String Upper & String Lower

def ubah_huruf(teks):
    return teks.upper(), teks.lower()

# Judul Program
print("\033[1;34mProgram 20: Menggunakan Fungsi str.upper() dan str.lower()\033[0m")
teks_input = input("Masukkan sebuah string: ")
upper_case, lower_case = ubah_huruf(teks_input)
print("String dalam huruf besar:", upper_case)
print("String dalam huruf kecil:", lower_case)