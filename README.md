# 7_TugasSocketProgramming

# SamsungChat - Aplikasi Chat Sederhana Berbasis UDP
SamsungChat adalah aplikasi chat sederhana berbasis protokol UDP, yang terdiri dari dua bagian utama: server dan client. Aplikasi ini memungkinkan beberapa pengguna untuk bergabung dalam satu chatroom, mengirim dan menerima pesan secara real-time, serta memanfaatkan autentikasi dasar berbasis username dan password.

****Disusun oleh:****
Allodya Qonnita Arofa (18223054) dan
Rayhan Hidayatul Fikri (18223022)

## 📋 Fitur Utama
- **Autentikasi Pengguna**: 
  - Pengguna harus login dengan username unik dan password yang sama untuk dapat bergabung ke dalam chatroom.
  - Username yang sudah digunakan tidak dapat digunakan oleh pengguna lain.
- **Pengiriman Pesan Real-time**: 
  - Klien dapat mengirim dan menerima pesan melalui server, yang akan meneruskan pesan tersebut ke semua klien yang terhubung.
- **Koneksi Dinamis**: 
  - Pengguna dapat memasukkan alamat IP dan port server secara manual, memungkinkan aplikasi ini digunakan di berbagai pengaturan jaringan.
- **Antarmuka Grafis (GUI)**: 
  - Dibangun dengan `tkinter` untuk menyediakan tampilan antarmuka yang mudah digunakan, baik untuk sisi server maupun klien.

## 🗂️ Struktur Proyek
- `server.py`: 
  - Menyediakan fungsionalitas server, termasuk menangani autentikasi pengguna dan mengirimkan pesan ke semua klien.
- `client.py`: 
  - Aplikasi klien yang memungkinkan pengguna untuk terhubung ke server, melakukan login, dan berkomunikasi dengan pengguna lain dalam chatroom.

## ⚙️ Cara Kerja
### Server
1. Server mendengarkan koneksi dari klien pada alamat IP `0.0.0.0` dan port `11111`.
2. Server memverifikasi login klien berdasarkan password yang telah ditentukan (`samsungdagostore`).
3. Jika username sudah digunakan, server akan mengirimkan pesan `"USERNAME_TAKEN"` kepada klien.
4. Jika login berhasil, server menyimpan alamat klien dan memungkinkan klien tersebut untuk mengirim dan menerima pesan.
5. Setiap pesan dari klien akan diteruskan ke semua klien lain yang terhubung (kecuali pengirim).

### Client
1. Pengguna memasukkan alamat IP dan port server, serta username dan password melalui antarmuka grafis (`tkinter`).
2. Aplikasi klien mengirimkan permintaan login ke server.
3. Jika login berhasil, klien dapat mulai mengirim pesan ke server, yang kemudian akan diteruskan ke klien lain.
4. Pesan yang diterima dari server akan ditampilkan di area chat GUI klien.
5. Jika username sudah digunakan atau login gagal, klien akan menampilkan pesan kesalahan dan meminta pengguna untuk memasukkan data yang benar.

## 🛠️ Cara Menjalankan
### Persyaratan
- Python 3.x harus sudah terpasang pada komputer.
- Klien dan server dapat dijalankan di komputer yang berbeda selama berada dalam satu jaringan yang sama.

### Menjalankan Server
1. Clone repositori ini dan buka direktori proyek.
2. Jalankan `server.py` dengan perintah:
   ```bash
   python server.py
3. Server akan mulai mendengarkan koneksi pada port 11111 dan menampilkan log aktivitas di antarmuka grafis.

### Menjalankan Client
1. Clone repositori ini dan buka direktori proyek.
2. Jalankan client.py dengan perintah:
   ```bash
   python client.py
3. Masukkan alamat IP dan port server, username, dan password.
4. Jika login berhasil, Anda akan diarahkan ke area chat di mana Anda bisa mengirim dan menerima pesan dari pengguna lain.


