# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Clipping Nilai Pixel

while True:
    def clipping_pixel(nilai_pixel):
        if nilai_pixel > 255:
            return 255
        elif nilai_pixel < 0:
            return 0
        else:
            return nilai_pixel

    nilai_pixel = int(input("\nMasukkan nilai pixel hasil operasi: "))
    hasil_clipped = clipping_pixel(nilai_pixel)

    print(f"\nNilai pixel setelah clipping: {hasil_clipped}")