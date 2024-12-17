# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Error Handling Raise

def cek_positif(angka):
    if angka < 0:
        raise ValueError("Angka harus positif.")

# Judul Program
print("\033[1;34mProgram 35: Menggunakan raise untuk Menghasilkan Kesalahan\033[0m")
try:
    angka_input = float(input("Masukkan angka positif: "))
    cek_positif(angka_input)
    print("Angka yang dimasukkan adalah:", angka_input)
except ValueError as e:
    print(f"Kesalahan: {e}")