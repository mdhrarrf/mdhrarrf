# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Input Tanggal & Bulan

while True:
    def jumlah_hari_bulan(bulan, tahun):

        # Menentukan jumlah hari dalam bulan berdasarkan nomor bulan
        if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
            return 31

        elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
            return 30

        elif bulan == 2:
            # Memeriksa apakah tahun adalah tahun kabisat
            if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
                return 29

            else:
                return 28

        else:
            print("\nBulan tidak valid")  # Mengembalikan pesan jika bulan tidak valid

    def main():
        # Membaca input dari pengguna
        try:
            bulan = int(input("\nMasukkan nomor bulan (1-12): "))
            tahun = int(input("Masukkan tahun: "))
            
            # Validasi bulan
            if bulan < 1 or bulan > 12:
                print("\nBulan tidak valid. Harap masukkan nomor bulan antara 1 hingga 12.")
            else:
                # Menghitung dan menampilkan jumlah hari
                hari = jumlah_hari_bulan(bulan, tahun)
                print(f"\nJumlah hari pada bulan {bulan} tahun {tahun} adalah {hari}.")
        except ValueError:
            print("\nInput tidak valid. Harap masukkan angka untuk bulan dan tahun.")

    # Menjalankan fungsi utama
    main()