# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function Any & All

def cek_kondisi(angka):
    return any(angka), all(angka)

# Judul Program
print("\033[1;34mProgram 8: Menggunakan Fungsi any() dan all()\033[0m")
angka_input = list(map(int, input("Masukkan angka-angka (pisahkan dengan spasi): ").split()))
ada_positif, semua_positif = cek_kondisi([x > 0 for x in angka_input])
print("Ada angka positif:", ada_positif)
print("Semua angka positif:", semua_positif)