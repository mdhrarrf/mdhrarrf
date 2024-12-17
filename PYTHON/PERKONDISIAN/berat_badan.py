# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Berat Badan BMI

def kategori_berat_badan(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Judul Program
print("\033[1;34mProgram 7: Menentukan Kategori Berat Badan Berdasarkan BMI\033[0m")
# Input dari pengguna
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))
bmi = berat / (tinggi ** 2)
print(kategori_berat_badan(bmi))