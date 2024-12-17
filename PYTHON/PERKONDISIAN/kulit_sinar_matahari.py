# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Paparan Sinar

def kategori_paparan_sinar(paparan):
    if paparan < 1:
        return "Kesehatan Kulit: Sangat Baik"
    elif 1 <= paparan < 3:
        return "Kesehatan Kulit: Baik"
    elif 3 <= paparan < 5:
        return "Kesehatan Kulit: Cukup"
    else:
        return "Kesehatan Kulit: Buruk"

# Judul Program
print("\033[1;34mProgram 36: Menentukan Kategori Kesehatan Kulit Berdasarkan Paparan Sinar Matahari\033[0m")
# Input dari pengguna
paparan_input = float(input("Masukkan jumlah jam paparan sinar matahari per minggu: "))
print(kategori_paparan_sinar(paparan_input))