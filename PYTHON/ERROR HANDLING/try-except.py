# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Error Handling Try & Except

def bagi(a, b):
    return a / b

# Judul Program
print("\033[1;34mProgram 33: Penanganan Kesalahan dengan try dan except\033[0m")
try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    hasil = bagi(angka1, angka2)
    print("Hasil pembagian:", hasil)
except ZeroDivisionError:
    print("Kesalahan: Tidak dapat membagi dengan nol.")
except ValueError:
    print("Kesalahan: Masukkan angka yang valid.")
except Exception as e:
    print(f"Kesalahan tidak terduga: {e}")