# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Status Karyawan

def status_karyawan(masa_kerja):
    if masa_kerja < 1:
        return "Status: Karyawan Baru"
    elif 1 <= masa_kerja < 5:
        return "Status: Karyawan Menengah"
    else:
        return "Status: Karyawan Senior"

# Judul Program
print("\033[1;34mProgram 12: Menentukan Status Karyawan Berdasarkan Masa Kerja\033[0m")
# Input dari pengguna
masa_kerja_input = float(input("Masukkan masa kerja Anda (dalam tahun): "))
print(status_karyawan(masa_kerja_input))