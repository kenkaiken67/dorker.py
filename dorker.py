import os
import time
import socket
import platform
from urllib.parse import quote

def clean_domain(domain):
    """Membersihkan input domain dari protokol dan spasi"""
    return domain.replace("https://", "").replace("http://", "").strip().strip("/")

def is_target_alive(domain):
    """Mengecek apakah domain aktif/bisa dijangkau sebelum dorking"""
    print(f"[*] Melakukan ping ke {domain}...")
    try:
        socket.gethostbyname(domain)
        print("[+] Mantap! Target aktif dan merespons. Lanjut dorking...\n")
        return True
    except socket.gaierror:
        print("[-] ERROR: Domain tidak ditemukan atau sedang mati/offline.")
        return False

def force_open_brave(url, nama_dork):
    """Memaksa sistem operasi membuka browser BRAVE (Support WSL)"""
    print(f"👉 Membuka di Brave: {nama_dork}")
    try:
        os_type = platform.system()
        release_info = platform.release().lower()
        
        if "microsoft" in release_info or "wsl" in release_info:
            cmd = f'powershell.exe -Command "Start-Process brave \'{url}\'"'
            os.system(cmd)
            
        elif os_type == "Windows":
            cmd = f'powershell.exe -Command "Start-Process brave \'{url}\'"'
            os.system(cmd)
            
        elif os_type == "Darwin": 
            os.system(f'open -a "Brave Browser" "{url}"')
            
        else: 
            os.system(f'brave-browser "{url}" &')
            
    except Exception as e:
        print(f"❌ Gagal mengeksekusi perintah untuk {nama_dork}: {e}")

def start_hunting_v7(domain):
    target = clean_domain(domain)
    
    print("\n" + "="*60)
    print(f"🚀 ULTIMATE DORKER v7 (6 TABS EDITION) | TARGET: {target}")
    print("="*60)
    
    if not is_target_alive(target):
        print("[-] Operasi dibatalkan. Silakan ganti target.")
        return 

    dorks = {
        "1. File PDF/Doc Terindex": f"site:{target} filetype:pdf OR filetype:doc",
        "2. Folder Tanpa Kunci (Index of)": f"site:{target} intitle:\"index of\"",
        "3. Halaman Login / Admin": f"site:{target} inurl:admin OR inurl:login",
        "4. File Backup & Database": f"site:{target} filetype:sql OR filetype:db OR filetype:bkp",
        "5. File Konfigurasi Sensitif": f"site:{target} filetype:env OR filetype:conf OR filetype:config",
        "6. File Log (Aktivitas Server)": f"site:{target} filetype:log"
    }

    print(f"[+] Menyiapkan {len(dorks)} tab pencarian di Brave...\n")
    
    for nama, query in dorks.items():
        query_encoded = quote(query)
        link = f"https://www.google.com/search?q={query_encoded}"
        
        force_open_brave(link, nama)
        time.sleep(2) 

    print("\n" + "="*60)
    print(f"✅ Selesai! Cek browser Brave kamu sekarang.")

if __name__ == "__main__":
    try:
        print("\n--- ADVANCED PASSIVE RECONNAISSANCE TOOL ---")
        target_user = input("Masukkan domain (contoh: target.com): ")
        
        if target_user:
            start_hunting_v7(target_user)
        else:
            print("[!] Domain tidak boleh kosong!")
            
    except KeyboardInterrupt:
        print("\n[!] Program dihentikan user.")
    except Exception as e:
        print(f"\n[!] Fatal Error Terdeteksi: {e}")