# Muhammad Haidar Almer Rafif
# 22/10/24
# Program Latihan Campuran

# ini adalah komentar
print('''
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
''')
print(456)
print('Hasil kali 3 dan 5 adalah', 3*5)
print(f'Hasil kali 7 dan 3 adalah {7*3} dan {5*7}')

# VARIABLE
# KONSTANTA
kota1 = 'Cianjur'
nilai = 100
isLogin = True
kota2 = 'Bandung'

print('kota kamu adalah kota', kota1)
print('kota kamu adalah kota', kota2)
print(f'kota kamu lahir ada di kota {kota1} dan kota {kota2}')

# variable biodata haidar
NamaLengkap = 'Muhammad Haidar Almer Rafif'
JenisKelamin = 'Laki-Laki'
Usia = 14
NilaiMatematika = 90.10
NilaiBahasainggris = 99.99
NilaiBahasaindonesia = 98.20
NilaiIPAS = 88.20
NilaiJumlah = NilaiMatematika+NilaiBahasainggris+NilaiBahasaindonesia+NilaiIPAS

# KALIMAT
print(f'''
      \nNama saya adalah {NamaLengkap}, berjenis kelamin {JenisKelamin}, sekarang usia saya adalah {Usia}.
''')
print('\nNilai ujian terakhir saya adalah sebagai berikut:')
print(f'''\nMatematika : {NilaiMatematika}\nB. Indonesia: {NilaiBahasaindonesia}\nB. Inggris: {NilaiBahasainggris}\nIPAS: {NilaiIPAS}\n\nJumlah: {round(NilaiJumlah,2)}\nRata-rata: {round(NilaiJumlah/4,2)}
''')