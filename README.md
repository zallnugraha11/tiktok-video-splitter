# TikTok Video Splitter

## Deskripsi
Skrip ini digunakan untuk secara otomatis membagi video menjadi beberapa bagian dengan durasi 3 menit, mengubahnya ke format vertikal (1080x1920) sesuai aturan TikTok, serta menambahkan overlay teks seperti judul, nomor part, dan ajakan follow.

## Fitur
- **Memotong video** menjadi bagian berdurasi 3 menit.
- **Menyesuaikan format video ke vertikal** (1080x1920) tanpa distorsi.
- **Menambahkan overlay teks**:
  - Judul video di bagian atas.
  - Nomor part di bagian bawah.
  - Ajakan "Follow untuk lebih banyak konten!" di tengah.

## Prasyarat
Skrip ini memerlukan **FFmpeg** untuk berjalan dengan baik.

### **Instalasi FFmpeg**
- **Windows**:
  1. Download FFmpeg dari [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
  2. Tambahkan FFmpeg ke `PATH` sistem.
- **Linux (Ubuntu/Debian)**:
  ```bash
  sudo apt update && sudo apt install ffmpeg
  ```
- **MacOS**:
  ```bash
  brew install ffmpeg
  ```

## Cara Penggunaan
1. Jalankan skrip Python:
   ```bash
   python script.py
   ```
2. Masukkan nama file video MP4.
3. Masukkan nama folder untuk hasil output.
4. Masukkan judul video yang ingin ditampilkan di overlay.
5. Tunggu proses selesai.

## Contoh Output
Setiap video akan disimpan dalam folder output dengan format:
- `part_1.mp4`
- `part_2.mp4`
- `part_3.mp4`

Setiap bagian video memiliki:
- **Judul di bagian atas**
- **Part number di bagian bawah**
- **Ajakan follow di tengah**

## Lisensi
Skrip ini dapat digunakan dan dimodifikasi secara bebas.

