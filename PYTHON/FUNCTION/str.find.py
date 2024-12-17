# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function String Find

def cari_kata(teks, kata):
    return teks.find(kata)

# Judul Program
print("\033[1;34mProgram 22: Menggunakan Fungsi str.find()\033[0m")
teks_input = input("Masukkan sebuah kalimat: ")
kata_input = input("Masukkan kata yang ingin dicari: ")
index = cari_kata(teks_input, kata_input)
if index != -1:
    print(f"Kata '{kata_input}' ditemukan pada index {index}.")
else:
    print(f"Kata '{kata_input}' tidak ditemukan.")