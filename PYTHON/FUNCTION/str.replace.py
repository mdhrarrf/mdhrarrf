# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function String Replace

def ganti_kata(teks, kata_lama, kata_baru):
    return teks.replace(kata_lama, kata_baru)

# Judul Program
print("\033[1;34mProgram 21: Menggunakan Fungsi str.replace()\033[0m")
teks_input = input("Masukkan sebuah kalimat: ")
kata_lama = input("Masukkan kata yang ingin diganti: ")
kata_baru = input("Masukkan kata pengganti: ")
print("Kalimat setelah penggantian:", ganti_kata(teks_input, kata_lama, kata_baru))