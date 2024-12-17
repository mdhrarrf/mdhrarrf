# Muhammad Haidar Almer Rafif
# 17/12/24
# Program Belajar Function Zip

def gabungkan_list(list1, list2):
    return list(zip(list1, list2))

# Judul Program
print("\033[1;34mProgram 7: Menggunakan Fungsi zip()\033[0m")
list1_input = input("Masukkan elemen list 1 (pisahkan dengan spasi): ").split()
list2_input = input("Masukkan elemen list 2 (pisahkan dengan spasi): ").split()
gabungan = gabungkan_list(list1_input, list2_input)
print("Gabungan dari kedua list adalah:", gabungan)