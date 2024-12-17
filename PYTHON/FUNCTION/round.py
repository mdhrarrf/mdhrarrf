# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function Round

def pembulatan(angka, desimal):
    return round(angka, desimal)

# Judul Program
print("\033[1;34mProgram 10: Menggunakan Fungsi round()\033[0m")
angka_input = float(input("Masukkan angka: "))
desimal_input = int(input("Masukkan jumlah desimal yang diinginkan: "))
print("Hasil pembulatan:", pembulatan(angka_input, desimal_input))