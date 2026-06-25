# Socket Programming using UDP and TCP

## Link Source Code

- [`UDPClient.py`](../assets/week6/UDPClient.py)
- [`UDPServer.py`](../assets/week6/UDPServer.py)
- [`TCPClient.py`](../assets/week6/TCPClient.py)
- [`TCPServer.py`](../assets/week6/TCPServer.py)

---

## Cara Menjalankan
1. **Jalankan Server**
   - UDP:  
     ```bash
     python UDPServer.py
     ```
   - TCP:  
     ```bash
     python TCPServer.py
     ```

2. **Jalankan Client**
   - UDP:  
     ```bash
     python UDPClient.py
     ```
   - TCP:  
     ```bash
     python TCPClient.py
     ```

3. **Input Data**
   - Hello World

---

## Implementasi UDP

### Konsep
- Tidak perlu koneksi  
- Mengirim data langsung  
- Tidak menjamin data sampai  

### Alur Program
1. Client input teks  
2. Client kirim ke server  
3. Server terima data  
4. Server ubah ke huruf besar  
5. Server kirim balik  

### Potongan Kode Client
```python
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(message.encode(), (serverName, serverPort))
```

### Potongan Kode Server
```python
message, clientAddress = serverSocket.recvfrom(2048)
modifiedMessage = message.decode().upper()
serverSocket.sendto(modifiedMessage.encode(), clientAddress)
```

---

## Implementasi TCP

### Konsep
- Harus membuat koneksi  
- Data lebih aman  
- Urutan data terjamin  

### Alur Program
1. Client connect ke server  
2. Server menerima koneksi  
3. Client kirim data  
4. Server proses data  
5. Server kirim balik  

### Potongan Kode Client
```python
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send(sentence.encode())
```

### Potongan Kode Server
```python
serverSocket.listen(1)
connectionSocket, addr = serverSocket.accept()
sentence = connectionSocket.recv(1024).decode()
```

---

## Perbedaan UDP dan TCP

| Aspek        | UDP              | TCP                  |
|--------------|------------------|----------------------|
| Koneksi      | Tidak ada        | Ada (handshake)      |
| Kecepatan    | Lebih cepat      | Lebih lambat         |
| Keandalan    | Tidak dijamin    | Dijamin              |
| Urutan data  | Tidak dijamin    | Teratur              |

---

## Contoh Output

**Input dari client:**
```
hello world
```

**Output dari server:**
```
HELLO WORLD
```

---

## Screenshot

Contoh:

**Output TCP** ![output](../assets/week6/TCP.png)  
**Output UDP** ![output](../assets/week6/UDP.png) 

---

## Kesimpulan
- Socket digunakan untuk komunikasi antar proses  
- UDP cocok untuk kebutuhan cepat  
- TCP cocok untuk kebutuhan stabil  
- Program ini menunjukkan dasar komunikasi jaringan  
```
