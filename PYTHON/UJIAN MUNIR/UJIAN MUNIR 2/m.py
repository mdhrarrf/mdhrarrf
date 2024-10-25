# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Mengkonversi Panjang

while True:
    INCI_METER = 25.4
    KAKI_INCI = 30.48
    YARD_KAKI = 0.9144

    meter = float(input("\nMasukkan panjang benda dalam meter: "))

    inci = meter*INCI_METER
    kaki = inci/KAKI_INCI
    yard = kaki/YARD_KAKI

    print(f"\nPanjang dalam inci: {inci:.2f} mm")
    print(f"Panjang dalam kaki: {kaki:.2f} cm")
    print(f"Panjang dalam yard: {yard:.2f} m")