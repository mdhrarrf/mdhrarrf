# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Status Lulus

def status_lulus(nilai):
    if nilai >= 75:
        return "Anda Lulus"
    else:
        return "Anda Tidak Lulus"

# Judul Program
print("\033[1;34mProgram 8: Menentukan Status Lulus Berdasarkan Nilai Ujian\033[0m")
# Input dari pengguna
nilai_input = float(input("Masukkan nilai ujian Anda: "))
print(status_lulus(nilai_input))