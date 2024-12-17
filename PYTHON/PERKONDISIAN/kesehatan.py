# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Status BMI

def status_bmi(bmi):
    if bmi < 18.5:
        return "Anda termasuk kategori underweight."
    elif 18.5 <= bmi < 24.9:
        return "Anda termasuk kategori normal."
    elif 25 <= bmi < 29.9:
        return "Anda termasuk kategori overweight."
    else:
        return "Anda termasuk kategori obesitas."

# Judul Program
print("\033[1;34mProgram 3: Menentukan Status Kesehatan Berdasarkan BMI\033[0m")
# Input dari pengguna
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))
bmi = berat / (tinggi ** 2)
print(status_bmi(bmi))