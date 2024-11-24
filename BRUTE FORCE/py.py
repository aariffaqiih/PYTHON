"""
Program Brute Force untuk Menemukan Password File RAR
-----------------------------------------------------
Program ini mencoba mengekstrak file RAR dengan menggunakan metode brute force.
Password akan dicoba secara bertahap mulai dari angka 00000 hingga 99999.

Panduan Penggunaan:
1. Pastikan Python terinstal di sistem Anda. Unduh dari https://www.python.org/.
2. Instal library tambahan menggunakan pip jika diperlukan (semua library yang digunakan adalah bawaan Python).
3. Letakkan file RAR yang ingin diuji di direktori yang sama dengan script ini.
4. Ubah nama file RAR pada variabel `file_rar` agar sesuai dengan nama file Anda.

Library yang Digunakan:
- subprocess: Untuk menjalankan perintah sistem.
- os: Untuk operasi file dan direktori.

Langkah-langkah:
1. Program memeriksa apakah file RAR dan WinRAR terinstal di sistem.
2. Jika semua persiapan sudah lengkap, program mencoba password mulai dari angka 00000.
3. Jika password benar, file akan diekstrak ke folder 'Extracted'.
4. Jika password salah, program melanjutkan ke percobaan berikutnya hingga menemukan password atau selesai.

Catatan:
- Gunakan software auto-clicker sebagai alat bantu.
- File WinRAR harus terinstal di lokasi default (atau sesuaikan path-nya di variabel `winrar_path`).
"""

# Import library yang diperlukan

import subprocess  # Library untuk menjalankan perintah sistem
import os          # Library untuk operasi file dan direktori

# Fungsi utama brute force untuk mencoba password RAR
def brute_force_rar(file_name):
    """
    Fungsi utama untuk melakukan brute force pada file RAR.
    file_name: Nama file RAR yang ingin dibuka.
    """

    # 1. Menentukan path ke WinRAR yang terinstal di komputer
    # Path ini menunjukkan lokasi aplikasi WinRAR yang akan dipakai untuk membuka file RAR.
    winrar_path = r"C:\\Program Files\\WinRAR\\WinRAR.exe"  # Sesuaikan lokasi jika berbeda
    
    # 2. Memeriksa apakah WinRAR ada di path yang diberikan
    # Fungsi os.path.exists akan mengecek apakah file WinRAR ada di lokasi yang disebutkan.
    if not os.path.exists(winrar_path):
        print("WinRAR tidak ditemukan di path yang diberikan.")  # Pesan kesalahan jika WinRAR tidak ditemukan
        return

    # 3. Mendapatkan direktori file RAR
    # Fungsi os.getcwd() akan memberi tahu kita di mana script Python sedang berjalan.
    # File RAR harus ada di direktori yang sama dengan script Python.
    current_dir = os.getcwd()  # Mendapatkan direktori saat ini
    
    # 4. Membuat path lengkap untuk file RAR
    # Menggabungkan direktori tempat script dijalankan dan nama file RAR menjadi path lengkap.
    file_path = os.path.join(current_dir, file_name)
    
    # 5. Memeriksa apakah file RAR benar ada
    if not os.path.exists(file_path):
        print(f"File {file_name} tidak ditemukan di folder ini.")  # Pesan kesalahan jika file RAR tidak ada
        return

    # 6. Membuat folder output untuk ekstraksi
    # Menggabungkan direktori saat ini dengan nama folder "Extracted".
    # Fungsi os.makedirs akan membuat folder "Extracted" jika belum ada.
    output_folder = os.path.join(current_dir, "Extracted")
    os.makedirs(output_folder, exist_ok=True)  # Membuat folder untuk hasil ekstraksi, jika belum ada

    # 7. Brute force password dari 80000 hingga 99999
    # Menggunakan range untuk mencoba password mulai dari 80000 hingga 99999.
    # Password akan diubah menjadi string 5 digit dengan padding leading zero jika diperlukan.
    for password in range(00000, 100000):  # Password akan dicoba mulai dari 80000 hingga 99999
        password_str = f"{password:05d}"  # Mengubah angka menjadi string dengan 5 digit

        try:
            # 8. Menyusun perintah untuk menjalankan WinRAR
            # Perintah ini akan mengekstrak file RAR dengan password yang dicoba.
            # Formatnya adalah: WinRAR.exe x -pPASSWORD file.rar output_folder
            command = [
                winrar_path,       # Lokasi aplikasi WinRAR
                "x",               # Perintah untuk ekstrak file
                f"-p{password_str}", # Password yang sedang diuji
                file_path,         # Lokasi file RAR
                output_folder,     # Folder untuk hasil ekstraksi
            ]

            # 9. Menampilkan password yang sedang diuji
            # Ini hanya untuk memberi tahu pengguna password apa yang sedang diuji
            print(f"Mencoba password: {password_str}")
            
            # 10. Menjalankan perintah
            # subprocess.run akan menjalankan perintah di command dan menunggu hasilnya.
            # stdout=subprocess.PIPE dan stderr=subprocess.PIPE menangkap output dari perintah.
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # 11. Memeriksa apakah ekstraksi berhasil
            # Jika returncode hasilnya 0, itu berarti perintah berhasil dijalankan.
            if result.returncode == 0:
                print(f"Password ditemukan: {password_str}")  # Menampilkan password yang berhasil
                return  # Jika password ditemukan, keluar dari fungsi

        except Exception as e:
            # 12. Menangani error jika terjadi kesalahan dalam menjalankan perintah
            print(f"Terjadi kesalahan: {e}")  # Menampilkan pesan error jika ada kesalahan

    # 13. Jika loop selesai dan tidak menemukan password yang benar
    print("Password tidak ditemukan.")  # Jika tidak ada password yang berhasil ditemukan

# 14. Nama file RAR yang ingin diuji
# Gantilah nama file ini dengan nama file RAR yang Anda miliki
file_rar = "txt.rar"

# 15. Memanggil fungsi brute_force_rar untuk memulai pencarian password
brute_force_rar(file_rar)  # Menjalankan brute force untuk file RAR yang ditentukan
