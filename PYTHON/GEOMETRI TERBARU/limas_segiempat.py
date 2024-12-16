# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Limas Segiempat

PHI = 3.14

def hitung_limas_segiempat(panjang, lebar, tinggi_limas):
    volume = round((1/3) * panjang * lebar * tinggi_limas)
    luas_permukaan = round(panjang * lebar + 2 * (panjang + lebar) * (tinggi_limas ** 2) ** 0.5)
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Limas Segiempat\033[0m")
print("-------------------------------------------------------------")
while True:
    panjang_limas = float(input("Masukkan panjang limas: "))
    lebar_limas = float(input("Masukkan lebar limas: "))
    tinggi_limas_segiempat = float(input("Masukkan tinggi limas: "))
    volume_limas_segiempat, luas_permukaan_limas_segiempat = hitung_limas_segiempat(panjang_limas, lebar_limas, tinggi_limas_segiempat)
    print("\nLimas Segiempat:")
    print(f"Volume:\t\t{volume_limas_segiempat}")
    print(f"Luas Permukaan:\t{luas_permukaan_limas_segiempat}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_limas_segiempat()