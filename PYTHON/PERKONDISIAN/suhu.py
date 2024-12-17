# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Suhu

def kategori_suhu(suhu):
    if suhu < 0:
        return "Suhu: Beku"
    elif 0 <= suhu < 20:
        return "Suhu: Dingin"
    elif 20 <= suhu < 30:
        return "Suhu: Hangat"
    else:
        return "Suhu: Panas"

# Judul Program
print("\033[1;34mProgram 13: Menentukan Kategori Suhu\033[0m")
# Input dari pengguna
suhu_input = float(input("Masukkan suhu dalam derajat Celsius: "))
print(kategori_suhu(suhu_input))