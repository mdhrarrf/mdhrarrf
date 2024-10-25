# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Diskon

while True:
    def hitung_diskon(total_belanja):

        # Menentukan diskon
        if total_belanja > 100000:
            diskon = total_belanja * 0.10  # Diskon 10%
        else:
            diskon = 0
        
        # Menghitung harga setelah diskon
        harga_setelah_diskon = total_belanja - diskon
        
        return diskon, harga_setelah_diskon

    def main():
        try:
            # Membaca input dari pengguna
            total_belanja = float(input("\nMasukkan total belanja: Rp. "))
            
            # Validasi input
            if total_belanja < 0:
                raise ValueError("Total belanja tidak boleh negatif.")
            
            # Menghitung diskon dan harga setelah diskon
            diskon, harga_setelah_diskon = hitung_diskon(total_belanja)
            
            # Menampilkan hasil
            print(f"\nDiskon: Rp. {diskon:.2f}")
            print(f"\nTotal belanja setelah dikurangi diskon: Rp. {harga_setelah_diskon:.2f}")
        
        except ValueError as e:
            # Menangani kesalahan input
            print(f"\nError: {e}")

    # Menjalankan fungsi utama
    if __name__ == "__main__":
        main()