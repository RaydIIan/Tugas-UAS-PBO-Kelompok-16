# Tugas-UAS-PBO-Kelompok-16

UAS PBO

Sifat: Group Project (max 3 orang)
Waktu: 1 minggu

Buatlah game sederhana dengan menggunakan python dan buat laporan bagaimana konsep
OOP diterapkan pada pemrograman tersebut.

Silahkan pilih program di bawah ini:
1. Game Hangman menggunakan python: Saya yakin sebagian besar dari kita pernah
memainkan game klasik yang menggunakan skrip python ini. Kita tahu tujuan utama dari
permainan ini adalah untuk &#39;menebak kata&#39;, yang disebut dengan deretan tanda hubung, dan
kita perlu menebak huruf dari kata tersebut.
2. Notepad menggunakan Tkinter dengan Python: Tkinter adalah paket GUI dari python. Kita
dapat membuat notepad sederhana yang terdiri dari berbagai menu seperti cara menyimpan,
membuka, dan mengedit file.
3. Migrasi burung dilacak menggunakan Python: Peneliti menggunakan modul GPS untuk
melacak hewan seperti kapan dan ke bagian mana mereka bepergian. Kumpulan data Python
memberikan detail lokasi menggunakan GPS dan memberikan gambaran tentang tanggal,
waktu, lintang, bujur, dan kecepatan burung.
4. Mengedit gambar dengan Python: Perpustakaan Pencitraan Python menawarkan juru bahasa
untuk mengedit gambar. Ini membantu untuk membuka, memotong, mengubah ukuran,
mengambil ukuran dan menyimpan gambar.
5. Operasi dalam file Zip menggunakan python: File ZIP membantu mengurangi file besar dan
menyatukan file terkait. Dengan menggunakan program sederhana python kita dapat
melakukan operasi yang berbeda pada file zip.
6. Terjemahan DNA menggunakan python: Dengan menggunakan rumus python ini, kita dapat
menerjemahkan DNA menjadi RNA dan kemudian menjadi protein. Ini membantu untuk
mengubah urutan DNA tertentu menjadi protein yang setara.
7. Server ruang obrolan menggunakan Python: Menggunakan ide soket dan threading, skrip ini
membantu menyiapkan Ruang Obrolan sederhana yang memungkinkan beberapa klien untuk
terhubung. Kode ini bekerja dengan ide soket dan threading.
8. Untuk memburamkan gambar menggunakan Python: Dengan bantuan kernel filter low pass
yang berbeda, ini membuat gambar menjadi kurang jelas atau berbeda dan membuat gambar
halus.
9. Fasilitas pemesanan makanan menggunakan Python: Aplikasi ini membantu seseorang
memesan makanan di rumah tanpa membuang waktu di restoran.
10. Prediksi kanker payudara menggunakan Python: Proyek ilmu data ini membantu
mendeteksi Kanker Payudara menggunakan kumpulan data.
11. Penggunaan grafik dengan Python: Cara terbaik python adalah visualisasi. Ini termasuk
mempelajari berbagai tahapan pemrograman menggunakan pustaka python.
12. Membuat password dengan menggunakan Python: Dengan menggunakan skrip python ini
kita dapat membantu dalam pembuatan password dengan beberapa batasan seperti harus
campuran huruf besar, huruf kecil, simbol, dan angka.



Penjelasan Kode :

Pertama-tama yaitu import random, def hangman(): kemudian Pada baris 3 kata = ['python', 'java', 'pbo', 'javascript', 'html'] , kita mendefinisikan sebuah list kata yang berisi beberapa kata yang akan digunakan dalam permainan hangman. Setiap kata ini akan diambil secara acak oleh program untuk menjadi kata yang harus ditebak. Selanjutnya kata_terpilih = random.choice(kata) Pada baris itu, kita menggunakan fungsi random.choice(kata) untuk memilih sebuah kata secara acak dari list kata. Kata yang dipilih secara acak disimpan dalam variabel kata_terpilih. Setelah itu Pada baris 10 yaitu tebakan = '' , kita membuat variabel tebakan yang awalnya berisi string kosong. Nantinya, huruf-huruf yang ditebak oleh pemain akan disimpan dalam variabel ini. Langkah selanjutnya yaitu kesempatan = 6 , kita mendefinisikan variabel kesempatan yang diinisialisasi dengan nilai 6. Variabel ini akan digunakan untuk menghitung jumlah kesempatan yang tersisa bagi pemain.

Kemudian, while kesempatan > 0: loop while yang akan berjalan selama kesempatan masih lebih dari 0. Artinya, loop ini akan berjalan selama pemain masih memiliki kesempatan untuk menebak. Setelah itu gagal = 0 Di dalam loop, kita inisialisasi variabel gagal dengan nilai 0 . Variabel ini akan digunakan untuk menghitung jumlah huruf yang belum berhasil ditebak oleh pemain.

Langkah selanjutnya yaitu for huruf in kata_terpilih:, terdapat loop for yang akan melakukan iterasi pada setiap huruf dalam kata_terpilih. Kemudian if huruf in tebakan: Jika huruf tersebut sudah ada dalam tebakan, huruf tersebut akan dicetak. Ssetelah itu print(huruf, end=' '), else:, print('_', end=' ') Jika huruf belum ada dalam tebakan, maka akan dicetak sebagai garis bawah ('_'). Selain itu gagal += 1 , variabel gagal akan bertambah jika terdapat huruf yang belum ditebak. 

Setelah menampilkan keadaan kata yang harus ditebak, langkah selanjutnya yaitu gagal += 1, kita memeriksa apakah variabel gagal masih memiliki nilai 0. Jika iya, artinya semua huruf telah berhasil ditebak oleh pemain dan pemain memenangkan permainan. Kemudian print('\n\nAnda menang!')  akan mencetak  Pesan "Anda menang!", dan setelah itu break loop akan dihentikan dengan pernyataan break.

Jika variabel gagal tidak sama dengan 0, artinya masih terdapat huruf-huruf yang belum ditebak, maka kita meminta pemain untuk menebak huruf selanjutnya. Huruf yang ditebak oleh pemain diambil menggunakan fungsi tebak = input('\n\nTebak sebuah huruf: ') dan disimpan dalam variabel tebak. tebakan += tebak. Huruf yang ditebak kemudian ditambahkan ke dalam variabel tebakan. tebakan += tebak , untuk menyimpan semua huruf yang telah ditebak oleh pemain. Selanjutnya,  if tebak not in kata_terpilih: , kita memeriksa apakah huruf yang ditebak tidak ada dalam kata yang dipilih. Jika huruf tersebut tidak ada, setelah itu             kesempatan -= 1 berarti tebakan pemain salah. Jumlah kesempatan (kesempatan) dikurangi 1, menandakan bahwa pemain memiliki satu kesempatan kurang. Program juga mencetak pesan "Tebakan salah!" dan menampilkan jumlah kesempatan yang tersisa.

  Selain itu, jika pemain telah menggunakan semua kesempatan if kesempatan == 0: , program akan mencetak pesan "Anda kalah! Kata yang benar adalah" diikuti dengan kata yang seharusnya ditebak (kata_terpilih). print('\n\nAnda kalah! Kata yang benar adalah', kata_terpilih) Terakhir, di luar loop while, kita memanggil fungsi hangman() untuk memulai permainan hangman.
  
Jadi, kode di atas mengimplementasikan permainan hangman sederhana di mana pemain harus menebak huruf untuk mengungkapkan sebuah kata yang dipilih secara acak. Pemain diberikan 6 kesempatan untuk menebak huruf-huruf tersebut. Jika pemain berhasil menebak semua huruf dengan benar dalam kesempatan yang diberikan, mereka memenangkan permainan. Jika tidak, mereka kalah.
Printscreen Output


Penjelasan Output :

Dapat dilihat dari Gambar 2 bahwa Ketika program Game Hangman di jalankan akan pertama muncul beberapa Underscore_ (_) yang menunjukkan pengguna tentang berapa huruf yang terdapat dalam kata yang di tanyakan, selanjutnya ditampilkan kalimat Tebak Semua Huruf: dimana disana kita dapat meng-inputkan huruf yang menurut kita ada di dalam kata tersebut. Apabila huruf yang diinputkan ada di dalam kata, maka semua instansi huruf tersebut akan ditampilkan. Misalnya kata Java, Ketika kita menebak huruf A, maka pada instansi selanjutnya semua huruf a dalam kata tersebut akan ditampilkan menjadi _a_a. apabila huruf yang diinputkan tidak ada dalam kata, maka anda akan mendapatkan jawaban Tebakan Salah! Dan akan ditampilkan lagi beberapa kesempatan anda untuk menjawab teka tekinya Ketika salah. Proses ini dilakukan sampai pengguna dapat menebak semua huruf dari kata tersebut, dimana Ketika anda menang, program akan menampilkan Anda Menang! Dan apabila pengguna tidak dapat menebak huruf yang benar dalam semua kesempatan itu maka program akan memberikan output Anda Kalah! Kata yang benar adalah (kata).
