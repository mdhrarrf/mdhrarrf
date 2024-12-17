# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Grade Nilai

def grade_nilai(nilai):
    if nilai >= 85:
        return "Grade: A"
    elif nilai >= 70:
        return "Grade: B"
    elif nilai >= 60:
        return "Grade: C"
    elif nilai >= 50:
        return "Grade: D"
    else:
        return "Grade: F"

# Judul Program
print("\033[1;34mProgram 2: Menentukan Grade Berdasarkan Nilai\033[0m")
# Input dari pengguna
nilai_input = float(input("Masukkan nilai Anda: "))
print(grade_nilai(nilai_input))