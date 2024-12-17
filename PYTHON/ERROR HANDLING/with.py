# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Error Handling With

# Judul Program
print("\033[1;34mProgram 39: Menggunakan with untuk Penanganan Kesalahan pada File\033[0m")
try:
    with open("file_tidak_ada.txt", 'r') as file:
        konten = file.read()
except FileNotFoundError:
    print("Kesalahan: File tidak ditemukan.")
except Exception as e:
    print(f"Kesalahan tidak terduga: {e}")