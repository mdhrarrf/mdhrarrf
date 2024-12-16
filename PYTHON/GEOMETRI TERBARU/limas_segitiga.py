# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Limas Segitiga

PHI = 3.14

def hitung_limas_segitiga(alas, tinggi, tinggi_limas):
    volume = round((1/3) * (1/2) * alas * tinggi * tinggi_limas)
    luas_permukaan = round((1/2) * alas * tinggi + 3 * (1/2) * alas * tinggi)
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Limas Segitiga\033[0m")
print("-------------------------------------------------------------")
while True:
    alas_limas = float(input("Masukkan alas segitiga: "))
    tinggi_limas = float(input("Masukkan tinggi segitiga: "))
    tinggi_limas_segitiga = float(input("Masukkan tinggi limas: "))
    volume_limas_segitiga, luas_permukaan_limas_segitiga = hitung_limas_segitiga(alas_limas, tinggi_limas, tinggi_limas_segitiga)
    print("\nLimas Segitiga:")
    print(f"Volume:\t\t{volume_limas_segitiga}")
    print(f"Luas Permukaan:\t{luas_permukaan_limas_segitiga}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_limas_segitiga()