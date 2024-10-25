# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Menentukan Segitiga

while True:
    def jenis_segita(a, b, c):

        if a <= 0 or b <= 0 or c <= 0 or a > b or b > c:
            return "\nInput tidak valid"

        a2 = a ** 2
        b2 = b ** 2
        c2 = c ** 2

        if a2 + b2 == c2:
            return "\nSegitiga Siku-Siku"
        elif a2 + b2 > c2:
            return "\nSegitiga Lancip"
        else:
            return "\nSegitiga Tumpul"

    a = int(input("\nMasukkan panjang sisi a: "))
    b = int(input("Masukkan panjang sisi b: "))
    c = int(input("Masukkan panjang sisi c: "))

    print(jenis_segita(a, b, c))