# Laporan Praktikum Wireshark

## A. Pembukaan
Praktikum ini bertujuan untuk memahami cara kerja protokol jaringan secara langsung.  
Dengan menggunakan **Wireshark**, kita dapat menangkap dan menganalisis paket data yang dikirim dan diterima komputer saat mengakses internet.  
Melalui metode ini, terlihat bagaimana protokol seperti **HTTP, TCP, dan IP** saling bekerja dalam komunikasi jaringan.

---

## B. Langkah-Langkah Praktikum

### 1. Menjalankan aplikasi Wireshark
- Membuka browser web dan aplikasi Wireshark.  
- Pada tahap ini Wireshark belum menangkap paket jaringan.
![Menjalankan wireshark](../assets/week1/step1.png)

### 2. Memilih interface jaringan
- Pada menu **Capture**, pilih interface jaringan yang aktif (contoh: WiFi atau Ethernet).  
- Interface ini menjadi jalur lalu lintas data sehingga semua paket yang lewat bisa ditangkap.
![Memilih interface](../assets/week1/step2.png)

### 3. Memulai proses capture
- Setelah interface dipilih, proses capture dimulai.  
- Wireshark mulai merekam semua paket yang dikirim dan diterima komputer.
![Memulai capture](../assets/week1/step3.png)

### 4. Membuat aktivitas jaringan
- Untuk menghasilkan trafik jaringan, browser digunakan untuk membuka halaman: `https://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html`
- Saat halaman diakses, browser mengirim permintaan **HTTP** ke server, dan server mengirim balasan.  
- Semua proses ini ditangkap oleh Wireshark.
![Melakukan test pada link](../assets/week1/step4.png)

### 5. Menghentikan capture
- Setelah halaman berhasil dimuat, proses capture dihentikan.  
- Wireshark menampilkan daftar semua paket yang sudah direkam.
![Stop capture](../assets/week1/step5.png)

### 6. Melakukan filter paket
- Banyak paket muncul karena berbagai proses jaringan berjalan bersamaan.  
- Agar fokus pada HTTP, digunakan filter: `http`
- Setelah filter diterapkan, hanya paket HTTP yang ditampilkan.
![Filter paket](../assets/week1/step6.png)

### 7. Menganalisis paket HTTP
- Setelah filter diterapkan, terlihat dua paket utama.  
- Paket pertama adalah permintaan dari komputer ke server: `Source: 192.168.1.7 Destination: 128.119.245.12 Info: GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.`
- Ini menunjukkan browser mengirim permintaan **HTTP GET** untuk mengambil halaman web dari server `gaia.cs.umass.edu`.
![Analisis paket](../assets/week1/step7.png)

---

## C. Kesimpulan
Pada praktikum ini kita belajar menggunakan **Wireshark** untuk menangkap dan menganalisis paket jaringan.  
Hasil pengamatan menunjukkan adanya proses permintaan **HTTP GET** dari komputer ke server dan respon dari server.  
Hal ini memperlihatkan cara kerja komunikasi data dalam jaringan secara nyata.