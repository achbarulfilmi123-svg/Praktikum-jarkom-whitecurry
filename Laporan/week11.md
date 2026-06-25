# Modul 13 – Ethernet dan ARP (Wireshark)

## 1. Tujuan Praktikum
Mahasiswa dapat menginvestigasi cara kerja protokol Ethernet dan ARP menggunakan Wireshark.

---

## 2. Analisis Ethernet Frame

Pada bagian ini dilakukan capture paket saat mengakses sebuah halaman web menggunakan Wireshark. Tujuannya adalah mengamati frame Ethernet yang membawa data HTTP (khususnya HTTP GET request).

### 2.1 Capture Traffic di Wireshark

Wireshark dijalankan terlebih dahulu sebelum membuka URL berikut:

http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-lab-file3.html

Hasil capture awal:

![](../assets/week11/04-wireshark-start.png)

---

### 2.2 HTTP GET Request

Setelah halaman diakses, ditemukan paket HTTP GET yang dikirim dari komputer ke server.

HTTP GET packet:

![](../assets/week11/07-http-get-packet.png)

---

### 2.3 Detail Ethernet Frame

Packet HTTP GET kemudian dianalisis pada layer Ethernet untuk melihat informasi MAC address source dan destination.

Ethernet frame detail:

![](../assets/week11/08-ethernet-frame-details.png)

---

### 2.4 Filter Non-IP Protocol

Untuk fokus pada Ethernet dan ARP, protokol IP dinonaktifkan melalui menu *Analyze → Enabled Protocols*.

Tampilan setelah IP dimatikan:

![](../assets/week11/10-only-ethernet-arp-view.png)

---

## 3. Analisis ARP (Address Resolution Protocol)

ARP digunakan untuk melakukan mapping antara IP address dan MAC address di jaringan lokal.

---

### 3.1 ARP Cache Clearing

Sebelum analisis ARP dilakukan, cache ARP dihapus agar proses request dapat terlihat di Wireshark.

Perintah:
```
arp -d *
```

ARP cache setelah dibersihkan:

![](../assets/week11/11-arp-cache-cleared.png)

---

### 3.2 ARP Request

ARP Request adalah paket broadcast yang digunakan untuk mencari MAC address dari sebuah IP tertentu.

Pada hasil capture terlihat paket:

> Who has 192.168.1.11? Tell 192.168.1.1

Ini menunjukkan bahwa perangkat sedang meminta informasi MAC address dari IP 192.168.1.11.

ARP Request (broadcast):

![](../assets/week11/15-arp-request-broadcast.png)

---

### 3.3 ARP Reply

ARP Reply adalah respon dari perangkat yang memiliki IP yang diminta, berisi MAC address yang sesuai.

Pada capture terlihat:

> 192.168.1.11 is at 52:ff:da:f8:26:4b

Ini berarti perangkat dengan IP tersebut memberikan alamat MAC-nya.

ARP Reply:

![](../assets/week11/16-arp-reply.png)

---

## 4. Kesimpulan

- Ethernet digunakan untuk komunikasi data pada layer data link menggunakan MAC address.
- ARP berfungsi untuk menerjemahkan IP address menjadi MAC address.
- ARP Request digunakan untuk menanyakan pemilik IP tertentu.
- ARP Reply digunakan untuk memberikan jawaban berupa MAC address.
- Wireshark memungkinkan analisis detail komunikasi jaringan hingga layer Ethernet dan ARP.
```