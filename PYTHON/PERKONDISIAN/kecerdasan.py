# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori IQ

def kategori_iq(iq):
    if iq < 70:
        return "Kategori: Rendah"
    elif 70 <= iq < 90:
        return "Kategori: Di Bawah Rata-rata"
    elif 90 <= iq < 110:
        return "Kategori: Rata-rata"
    elif 110 <= iq < 130:
        return "Kategori: Di Atas Rata-rata"
    else:
        return "Kategori: Tinggi"

# Judul Program
print("\033[1;34mProgram 26: Menentukan Kategori Kecerdasan Berdasarkan Skor IQ\033[0m")
# Input dari pengguna
iq_input = int(input("Masukkan skor IQ Anda: "))
print(kategori_iq(iq_input))