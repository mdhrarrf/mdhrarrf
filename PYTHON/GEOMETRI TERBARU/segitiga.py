# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Segitiga

PHI = 3.14

def hitung_segitiga(alas, tinggi, sisi_a, sisi_b, sisi_c):
    luas = round(0.5 * alas * tinggi)
    keliling = round(sisi_a + sisi_b + sisi_c)
    return luas, keliling

print("\033[1;34mProgram Geometri: Menghitung Luas dan Keliling Segitiga\033[0m")
print("-------------------------------------------------------------")
while True:
    alas = float(input("Masukkan alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    sisi_a = float(input("Masukkan sisi a segitiga: "))
    sisi_b = float(input("Masukkan sisi b segitiga: "))
    sisi_c = float(input("Masukkan sisi c segitiga: "))
    luas_segitiga, keliling_segitiga = hitung_segitiga(alas, tinggi, sisi_a, sisi_b, sisi_c)
    print("\nSegitiga:")
    print(f"Luas:\t\t{luas_segitiga}")
    print(f"Keliling:\t{keliling_segitiga}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_segitiga()