# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Kesehatan Jantung

def kategori_kesehatan_jantung(detak_jantung):
    if detak_jantung < 60:
        return "Kesehatan Jantung: Di Bawah Normal"
    elif 60 <= detak_jantung <= 100:
        return "Kesehatan Jantung: Normal"
    else:
        return "Kesehatan Jantung: Di Atas Normal"

# Judul Program
print("\033[1;34mProgram 29: Menentukan Kategori Kesehatan Jantung Berdasarkan Detak Jantung\033[0m")
# Input dari pengguna
detak_jantung_input = int(input("Masukkan detak jantung Anda (denyut per menit): "))
print(kategori_kesehatan_jantung(detak_jantung_input))