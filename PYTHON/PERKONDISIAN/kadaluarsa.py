# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Perkondisian Kategori Kualitas Makanan

def kategori_kualitas_makanan(tanggal_kadaluarsa, tanggal_sekarang):
    if tanggal_kadaluarsa < tanggal_sekarang:
        return "Makanan sudah kadaluarsa."
    elif tanggal_kadaluarsa == tanggal_sekarang:
        return "Makanan harus segera digunakan."
    else:
        return "Makanan masih aman untuk dikonsumsi."

# Judul Program
print("\033[1;34mProgram 21: Menentukan Kategori Kualitas Makanan Berdasarkan Tanggal Kadaluarsa\033[0m")
# Input dari pengguna
tanggal_kadaluarsa_input = input("Masukkan tanggal kadaluarsa (YYYY-MM-DD): ")
tanggal_sekarang_input = input("Masukkan tanggal sekarang (YYYY-MM-DD): ")

# Mengonversi string ke format tanggal
from datetime import datetime
tanggal_kadaluarsa = datetime.strptime(tanggal_kadaluarsa_input, "%Y-%m-%d").date()
tanggal_sekarang = datetime.strptime(tanggal_sekarang_input, "%Y-%m-%d").date()

print(kategori_kualitas_makanan(tanggal_kadaluarsa, tanggal_sekarang))