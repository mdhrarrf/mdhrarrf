# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Error Handling Else

def bagi(a, b):
    return a / b

# Judul Program
print("\033[1;34mProgram 38: Penanganan Kesalahan dengan else\033[0m")
try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
except ValueError:
    print("Kesalahan: Masukkan angka yang valid.")
else:
    try:
        hasil = bagi(angka1, angka2)
    except ZeroDivisionError:
        print("Kesalahan: Tidak dapat membagi dengan nol.")
    else:
        print("Hasil pembagian:", hasil)