# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Berat Badan Ideal

while True:
    def pesan_berat_badan(berat_badan_ideal, berat_badan_sekarang):
        toleransi = 2
        
        if (berat_badan_ideal - toleransi) <= berat_badan_sekarang <= (berat_badan_ideal + toleransi):
            return "\nPesan Ideal: Berat badan Anda berada dalam rentang ideal."
        else:
            return "\nPesan Tidak Ideal: Berat badan Anda tidak berada dalam rentang ideal."

    berat_badan_ideal = float(input("\nMasukkan berat badan ideal (kg): "))
    berat_badan_sekarang = float(input("Masukkan berat badan sekarang (kg): "))

    pesan = pesan_berat_badan(berat_badan_ideal, berat_badan_sekarang)

    print(pesan)