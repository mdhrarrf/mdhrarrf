# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function Max & Min

def nilai_tertinggi_dan_terendah(angka):
    return max(angka), min(angka)

# Judul Program
print("\033[1;34mProgram 2: Menggunakan Fungsi max() dan min()\033[0m")
angka_input = list(map(int, input("Masukkan angka-angka (pisahkan dengan spasi): ").split()))
maks, mins = nilai_tertinggi_dan_terendah(angka_input)
print("Nilai tertinggi adalah:", maks)
print("Nilai terendah adalah:", mins)