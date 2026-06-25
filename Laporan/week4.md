# UDP Analysis Using Wireshark

## Soal
1. Pilih satu paket UDP yang terdapat pada trace Anda. Dari paket tersebut, berapa banyak “field” yang terdapat pada header UDP? Sebutkan nama-nama field yang Anda temukan!  
2. Perhatikan informasi “content field” pada paket yang Anda pilih di pertanyaan 1. Berapa panjang (dalam satuan byte) masing-masing “field” yang terdapat pada header UDP?  
3. Nilai yang tertera pada ”Length” menyatakan nilai apa? Verfikasi jawaban Anda melalui paket UDP pada trace.  
4. Berapa jumlah maksimum byte yang dapat disertakan dalam payload UDP? (Petunjuk: jawaban untuk pertanyaan ini dapat ditentukan dari jawaban Anda untuk pertanyaan 2)  
5. Berapa nomor port terbesar yang dapat menjadi port sumber? (Petunjuk: lihat petunjuk pada pertanyaan 4)  
6. Berapa nomor protokol untuk UDP? Berikan jawaban Anda dalam notasi heksadesimal dan desimal. Untuk menjawab pertanyaan ini, Anda harus melihat ke bagian ”Protocol” pada datagram IP yang mengandung segmen UDP.  
7. Periksa pasangan paket UDP di mana host Anda mengirimkan paket UDP pertama dan paket UDP kedua merupakan balasan dari paket UDP yang pertama. (Petunjuk: agar paket kedua merupakan balasan dari paket pertama, pengirim paket pertama harus menjadi tujuan dari paket kedua). Jelaskan hubungan antara nomor port pada kedua paket tersebut!  

---

## Jawaban
1. Header UDP terdiri dari empat field: **Source Port, Destination Port, Length, dan Checksum**.  
2. Setiap field pada header UDP memiliki panjang **2 byte**, sehingga total panjang header UDP adalah **8 byte**.  
3. Nilai **Length** menunjukkan total panjang segmen UDP (header + data). Contoh: Length = 58 byte → 8 byte header + 50 byte payload.  
4. Panjang maksimum payload UDP adalah **65527 byte** (65535 maksimum field Length – 8 byte header).  
5. Nomor port terbesar yang dapat digunakan adalah **65535** (karena field port = 16 bit).  
6. Nomor protokol untuk UDP adalah **17 (desimal)** dan **0x11 (heksadesimal)**.  
7. Hubungan port request–response:  
   - Request: Source Port = 4334, Destination Port = 161  
   - Response: Source Port = 161, Destination Port = 4334  
   - Menunjukkan pembalikan peran pengirim–penerima.  

---

## Bukti
- **Request:** ![UDP Request](../assets/week4/request.png)  
<<<<<<< HEAD
- **Response:** ![UDP Response](../assets/week4/respond.png)  
=======
- **Response:** ![UDP Response](../assets/week4/respond.png)  
>>>>>>> 7ba0d2e (malas cuy)
