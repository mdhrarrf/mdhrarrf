# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Balok

PHI = 3.14

def hitung_balok(panjang, lebar, tinggi):
    volume = round(panjang * lebar * tinggi)
    luas_permukaan = round(2 * (panjang * lebar + panjang * tinggi + lebar * tinggi))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Balok\033[0m")
print("-------------------------------------------------------------")
while True:
    panjang_balok = float(input("Masukkan panjang balok: "))
    lebar_balok = float(input("Masukkan lebar balok: "))
    tinggi_balok = float(input("Masukkan tinggi balok: "))
    volume_balok, luas_permukaan_balok = hitung_balok(panjang_balok, lebar_balok, tinggi_balok)
    print("\nBalok:")
    print(f"Volume:\t\t{volume_balok}")
    print(f"Luas Permukaan:\t{luas_permukaan_balok}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_balok()