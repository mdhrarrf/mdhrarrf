# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function String Strip

def bersihkan_teks(teks):
    return teks.strip()

# Judul Program
print("\033[1;34mProgram 23: Menggunakan Fungsi str.strip()\033[0m")
teks_input = input("Masukkan sebuah kalimat dengan spasi di awal atau akhir: ")
teks_bersih = bersihkan_teks(teks_input)
print("Kalimat setelah dibersihkan dari spasi:", teks_bersih)