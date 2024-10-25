# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Mengkonversi Digit ke Integer 

while True:
    def karakter_ke_integer(k):
        # Memastikan bahwa input adalah karakter digit
        if k.isdigit() and len(k) == 1:
            # Mengonversi karakter ke integer
            return int(k)
        else:
            raise ValueError("\n-99")

    # Contoh penggunaan
    karakter = input("\nMasukkan karakter digit ('0'..'9'): ")
    try:
        hasil = karakter_ke_integer(karakter)
        print(f"\nNilai integer: {hasil}")
    except ValueError as e:
        print(e)