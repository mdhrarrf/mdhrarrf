# Muhammad Haidar Almer Rafif
# 22/10/24
# Program Ujian Munir Soal 13

while True:
    HURUF_VOKAL = 'aiueoAIUEO'
    HURUF_KONSONAN = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

    huruf = input('\nMasukan Huruf\t: ')

    if huruf in HURUF_VOKAL:
        print('Huruf vokal')
    elif huruf in HURUF_KONSONAN:
        print('Huruf konsonan')
    else:
        print('Bukan berupa huruf')