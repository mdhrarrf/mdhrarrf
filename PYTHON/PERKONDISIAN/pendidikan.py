# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Pendidikan

def kategori_pendidikan(tingkat):
    if tingkat == "SD":
        return "Kategori: Sekolah Dasar"
    elif tingkat == "SMP":
        return "Kategori: Sekolah Menengah Pertama"
    elif tingkat == "SMA":
        return "Kategori: Sekolah Menengah Atas"
    elif tingkat == "D3":
        return "Kategori: Diploma 3"
    elif tingkat == "S1":
        return "Kategori: Sarjana"
    elif tingkat == "S2":
        return "Kategori: Magister"
    elif tingkat == "S3":
        return "Kategori: Doktor"
    else:
        return "Input tidak valid. Harap masukkan tingkat pendidikan yang benar."

# Judul Program
print("\033[1;34mProgram 16: Menentukan Kategori Pendidikan Berdasarkan Tingkat\033[0m")
# Input dari pengguna
tingkat_input = input("Masukkan tingkat pendidikan Anda (SD/SMP/SMA/D3/S1/S2/S3): ")
print(kategori_pendidikan(tingkat_input))