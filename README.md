# 🚀 Ultimate Dorker v7

**Advanced Passive Reconnaissance Tool** berbasis Python untuk mengotomatisasi pencarian informasi sensitif yang terekspos di mesin pencari menggunakan teknik Google Dorking. Script ini dirancang untuk langsung mengeksekusi 6 *query* pencarian spesifik secara berurutan di browser **Brave**.

## ✨ Fitur

- **Target Alive Check**: Memverifikasi apakah domain target aktif dan dapat dijangkau sebelum memulai proses dorking.
- **Cross-Platform Brave Integration**: Secara otomatis memaksa sistem operasi (mendukung Windows, macOS, Linux, dan WSL) untuk membuka hasil dorking langsung di browser Brave.
- **6 Tab Dorking Otomatis**:
  1. 📄 File PDF/Doc terindeks (`filetype:pdf OR filetype:doc`)
  2. 📂 Directory Listing (`intitle:"index of"`)
  3. 🔐 Halaman Login / Admin (`inurl:admin OR inurl:login`)
  4. 🗄️ File Backup & Database (`filetype:sql OR filetype:db OR filetype:bkp`)
  5. ⚙️ File Konfigurasi Sensitif (`filetype:env OR filetype:conf OR filetype:config`)
  6. 📝 File Log / Aktivitas Server (`filetype:log`)

## 🛠️ Prasyarat

- **Python 3.x** sudah terinstal di sistem.
- **Brave Browser** (Pastikan sudah terinstal agar script bisa membuka tab secara otomatis).

## 🚀 Cara Penggunaan

1. *Clone repository* ini ke *local machine* lu:
   ```bash
   git clone https://kenkaiken67.github.io/dorker.py/

2.Jalankan script
Script ini hanya menggunakan library bawaan Python, sehingga tidak perlu menginstal requirements.txt.
  ```bash
  python dorker.py
(Atau gunakan python3 dorker.py jika menggunakan Linux/macOS)

3.Masukkan Target
Saat program berjalan, Anda akan diminta memasukkan domain target.

Masukkan domain (contoh: target.com): example.com


🔍 Dork yang Digunakan (6 Tabs Edition)

File PDF/Doc Terindex: site:target.com filetype:pdf OR filetype:doc

Folder Tanpa Kunci: site:target.com intitle:"index of"

Halaman Login / Admin: site:target.com inurl:admin OR inurl:login

File Backup & Database: site:target.com filetype:sql OR filetype:db OR filetype:bkp

File Konfigurasi Sensitif: site:target.com filetype:env OR filetype:conf OR filetype:config

File Log (Aktivitas Server): site:target.com filetype:log

⚠️ Disclaimer (Peringatan Keamanan)

Script ini dibuat hanya untuk tujuan Edukasi, Riset Keamanan Siber, dan program Bug Bounty resmi.
Segala bentuk penyalahgunaan alat ini terhadap target yang tidak memiliki izin (ilegal) adalah di luar tanggung jawab pembuat alat (developer). Lakukan pengujian hanya pada sistem yang Anda miliki atau jika Anda telah mendapatkan izin tertulis secara eksplisit.
   
