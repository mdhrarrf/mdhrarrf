# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Error Handling Finally

def baca_file(nama_file):
    with open(nama_file, 'r') as file:
        return file.read()

# Judul Program
print("\033[1;34mProgram 34: Penanganan Kesalahan dengan finally\033[0m")
try:
    nama_file = input("Masukkan nama file yang ingin dibaca: ")
    konten = baca_file(nama_file)
    print("Isi file:", konten)
except FileNotFoundError:
    print("Kesalahan: File tidak ditemukan.")
except Exception as e:
    print(f"Kesalahan tidak terduga: {e}")
finally:
    print("Proses pembacaan file selesai.")