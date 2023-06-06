import random

def hangman():
    kata = ['python', 'java', 'pbo', 'javascript', 'html']
    kata_terpilih = random.choice(kata)  # Memilih kata secara acak dari daftar kata
    tebakan = ''  # Variabel untuk menyimpan huruf-huruf yang telah ditebak
    kesempatan = 6  # Jumlah kesempatan yang dimiliki pemain

    while kesempatan > 0:
        gagal = 0

        for huruf in kata_terpilih:
            if huruf in tebakan:
                print(huruf, end=' ')  # Menampilkan huruf jika sudah ditebak
            else:
                print('_', end=' ')  # Menampilkan garis bawah untuk huruf yang belum ditebak
                gagal += 1

        if gagal == 0:
            print('\n\nAnda menang!')  # Menampilkan pesan jika pemain menang
            break

        tebak = input('\n\nTebak sebuah huruf: ')  # Meminta pemain untuk menebak huruf
        tebakan += tebak

        if tebak not in kata_terpilih:
            kesempatan -= 1
            print('Tebakan salah!')  # Menampilkan pesan kesalahan jika huruf yang ditebak salah
            print('Anda memiliki', kesempatan, 'kesempatan lagi')

            if kesempatan == 0:
                print('\n\nAnda kalah! Kata yang benar adalah', kata_terpilih)  # Menampilkan pesan jika pemain kalah

hangman()
