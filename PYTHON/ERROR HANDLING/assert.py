# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Error Handling Assert

def cek_bilangan_genap(angka):
    assert angka % 2 == 0, "Angka harus genap."

# Judul Program
print("\033[1;34mProgram 37: Menggunakan assert untuk Validasi\033[0m")
try:
    angka_input = int(input("Masukkan angka genap: "))
    cek_bilangan_genap(angka_input)
    print("Angka yang dimasukkan adalah genap:", angka_input)
except AssertionError as e:
    print(f"Kesalahan: {e}")
except ValueError:
    print("Kesalahan: Masukkan angka yang valid.")