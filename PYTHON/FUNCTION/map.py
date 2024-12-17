# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function Map

def kuadrat(angka):
    return angka ** 2

# Judul Program
print("\033[1;34mProgram 5: Menggunakan Fungsi map()\033[0m")
angka_input = list(map(int, input("Masukkan angka-angka (pisahkan dengan spasi): ").split()))
kuadrat_input = list(map(kuadrat, angka_input))
print("Kuadrat dari angka-angka tersebut adalah:", kuadrat_input)