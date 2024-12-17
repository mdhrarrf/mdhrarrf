# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Kinerja

def kategori_kinerja(penilaian):
    if penilaian >= 90:
        return "Kategori: Sangat Baik"
    elif penilaian >= 75:
        return "Kategori: Baik"
    elif penilaian >= 60:
        return "Kategori: Cukup"
    else:
        return "Kategori: Buruk"

# Judul Program
print("\033[1;34mProgram 19: Menentukan Kategori Kinerja Karyawan Berdasarkan Penilaian\033[0m")
# Input dari pengguna
penilaian_input = float(input("Masukkan penilaian kinerja karyawan (0-100): "))
print(kategori_kinerja(penilaian_input))