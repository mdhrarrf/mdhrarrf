# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Kesehatan Paru

def kategori_kesehatan_paru(kebiasaan_merokok):
    if kebiasaan_merokok == 0:
        return "Kesehatan Paru-paru: Sangat Baik"
    elif 1 <= kebiasaan_merokok <= 5:
        return "Kesehatan Paru-paru: Baik"
    elif 6 <= kebiasaan_merokok <= 10:
        return "Kesehatan Paru-paru: Cukup"
    else:
        return "Kesehatan Paru-paru: Buruk"

# Judul Program
print("\033[1;34mProgram 33: Menentukan Kategori Kesehatan Paru-paru Berdasarkan Kebiasaan Merokok\033[0m")
# Input dari pengguna
kebiasaan_merokok_input = int(input("Masukkan jumlah rokok yang dihisap per hari: "))
print(kategori_kesehatan_paru(kebiasaan_merokok_input))