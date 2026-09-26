# 🛡️ ULTIMATE DORKER v7
### *Automated Passive Reconnaissance & Intelligence Gathering Engine*

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![OSINT](https://img.shields.io/badge/Security-OSINT%20Recon-red?style=for-the-badge&logo=shield)](https://github.com/)
[![Platform](https://img.shields.io/badge/Platform-Cross--Platform-informational?style=for-the-badge)](https://github.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

```text
  ██████╗  ██████╗ ██████╗ ██╗  ██╗███████╗██████╗ 
  ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
  ██║  ██║██║   ██║██████╔╝█████═╝ █████╗  ██████╔╝
  ██║  ██║██║   ██║██╔══██╗██╔═██╗ ██╔══╝  ██╔══██╗
  ██████╔╝╚██████╔╝██║  ██║██║ ╚██╗███████╗██║  ██║
  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ v7
  [ Passive OSINT Framework // Target Surface Discovery ]
```

---

## 📌 Executive Summary

**Ultimate Dorker v7** adalah instrumen *Passive Reconnaissance / Attack Surface Management* berbasis Python yang dirancang untuk mengotomatisasi pengumpulan intelijen terhadap target melalui teknik **Google Dorking**. 

Alat ini mengeliminasi proses manual dalam pencarian aset yang terekspos secara publik (*public exposure*), seperti file konfigurasi, database dumps, log server, dan direktori tanpa otentikasi, dengan langsung mengorkestrasi pencarian multi-tab secara terisolasi pada browser **Brave**.

---

## ⚡ Core Capabilities

- 🎯 **Pre-flight Target Validation**: Melakukan probing ketersediaan host sebelum rangkaian dork dieksekusi.
- 🌐 **Cross-Platform Native Browser Invocation**: Mengatur peluncuran sesi penelusuran native pada lingkungan Windows, macOS, Linux, maupun WSL.
- 🔎 **Zero-Noise Execution**: Karena bersifat pasif (*search-engine mediated*), aktivitas ini tidak menghasilkan query langsung yang menyentuh firewall/WAF target saat dorking berlangsung.
- ⚡ **Lightweight Footprint**: Beroperasi murni menggunakan library standar Python (tanpa dependensi eksternal).

---

## 🔬 Reconnaissance Vector Matrix

Alat ini memetakan 6 vektor eksposur data sensitif secara paralel:

| Vektor Target | Query Pattern | Potensi Risiko Dampak (Threat Impact) |
| :--- | :--- | :--- |
| **Document Harvesting** | `filetype:pdf OR filetype:doc` | Kebocoran data internal, kredensial tertulis, metadata dokumen (karyawan, software). |
| **Directory Indexing** | `intitle:"index of"` | Server misconfiguration yang membuka struktur direktori dan file mentah. |
| **Admin Endpoints** | `inurl:admin OR inurl:login` | Pemetaan titik otentikasi target untuk analisis brute-force / bypass. |
| **Database & Backups** | `filetype:sql OR filetype:db OR filetype:bkp` | *High Severity*: Potensi eksposur dump basis data mentah dan hash kata sandi. |
| **Sensitive Configs** | `filetype:env OR filetype:conf OR filetype:config` | *Critical Severity*: Kebocoran token API, credential database, dan secret keys. |
| **Server Logs** | `filetype:log` | Catatan aktivitas server, IP internal, jejak debug error, dan session IDs. |

---

## ⚙️ Environment Setup & Requirements

- **Runtime:** Python 3.8+
- **Browser:** [Brave Browser](https://brave.com/) terinstal pada default application path.
- **Dependencies:** `Standard Library Only` (tidak memerlukan `pip install`).

---

## 🚀 Deployment & Usage

### 1. Repository Acquisition
```bash
git clone https://github.com/kenkaiken67/dorker.py.git
cd dorker.py
```

### 2. Execution
Jalankan program melalui terminal dengan hak akses standar:

```bash
# Windows
python dorker.py

# Linux / macOS
python3 dorker.py
```

### 3. Target Specification
Masukkan domain target FQDN (*Fully Qualified Domain Name*) tanpa menyertakan skema URL (`http://` atau `https://`):

```text
[?] Target Host Domain: victim-organization.com
[*] Probing target status... [ONLINE]
[*] Launching automated OSINT tabs in Brave...
[+] Process completed successfully.
```

---

## 🛡️ Remediation & Countermeasures (Blue Team Guidance)

Bagi pengelola infrastruktur yang mendapati asetnya terindeks oleh teknik ini:

1. **Robots.txt & Meta Tags:** Konfigurasikan `X-Robots-Tag: noindex, nofollow` pada file atau direktori non-publik, serta atur direktori terlarang di `robots.txt`.
2. **Disable Directory Browsing:** Matikan fitur `Options Indexes` di Apache atau `autoindex off` di Nginx untuk mencegah pembacaan struktur folder.
3. **Web Server Root Hardening:** Pastikan file sensitif seperti `.env`, `.git`, dump database (`.sql`), dan arsip backup disimpan di luar *document root* (`public_html` / `www`).
4. **Google Removal Tool:** Manfaatkan *Google Search Console Removal Tool* untuk segera menghapus cache URL sensitif yang terlanjur terindeks.

---

## ⚖️ Legal Disclaimer & Rules of Engagement

> **IMPORTANT:** Alat ini dirancang khusus untuk keperluan **Security Auditing**, **Authorized Bug Bounty Programs**, dan **Edukasi Keamanan Informasi**.
> 
> Penggunaan alat ini terhadap target tanpa izin tertulis (*explicit authorization*) dapat melanggar hukum siber yang berlaku (seperti **UU ITE** di Indonesia atau **CFAA** secara internasional). Pengembang tidak bertanggung jawab atas tindakan destruktif atau penyalahgunaan yang dilakukan oleh pihak manapun.
