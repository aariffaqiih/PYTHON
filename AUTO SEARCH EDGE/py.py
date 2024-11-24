"""
Program Pencarian Otomatis di Bing dengan Selenium
--------------------------------------------------
Program ini akan membuka browser Microsoft Edge dan melakukan pencarian otomatis di Bing dengan kata kunci yang dibaca dari file teks.
Setiap kata kunci akan dimasukkan ke dalam kotak pencarian Bing dan pencarian akan dilakukan secara berurutan.

Langkah-langkah:
1. Pastikan Python dan Selenium sudah terinstal di komputer Anda.
2. Unduh Microsoft Edge WebDriver dan sesuaikan path-nya.
3. Siapkan file teks yang berisi kata kunci yang akan dicari di Bing.
4. Jalankan program dan biarkan ia melakukan pencarian otomatis untuk setiap kata kunci.

Library yang Digunakan:
- selenium: Untuk mengontrol browser dan melakukan pencarian.
- time: Untuk memberikan jeda waktu antar pencarian agar tidak terlalu cepat.

Catatan:
- Program ini mengandalkan Microsoft Edge sebagai browser dan memerlukan Edge WebDriver yang sesuai.
- Selenium dapat mengontrol browser untuk melakukan input teks dan interaksi dengan elemen web.
"""

# 1. Import library yang diperlukan
from selenium import webdriver  # Selenium untuk kontrol browser
from selenium.webdriver.edge.service import Service  # Service untuk menjalankan WebDriver Edge
from selenium.webdriver.common.keys import Keys  # Untuk menggunakan tombol "Enter" pada keyboard
import time  # Untuk memberi jeda waktu antar pencarian

# 2. Tentukan path ke Edge WebDriver
webdriver_path = "E:\FAQIH E\CODES\PYTHON\AUTO SEARCH EDGE\msedgedriver.exe"  # Path ke WebDriver Edge yang diunduh

# 3. Tentukan file yang berisi daftar kata kunci yang akan digunakan untuk pencarian
keywords_file = "E:\FAQIH E\CODES\PYTHON\AUTO SEARCH EDGE\keywords.txt"  # File teks yang berisi kata kunci

# 4. Inisialisasi WebDriver dan Service untuk menjalankan Edge browser
# Service digunakan untuk menjalankan WebDriver, yang diperlukan untuk Selenium agar dapat mengontrol browser.
service = Service(webdriver_path)  # Inisialisasi service dengan path WebDriver yang telah ditentukan
driver = webdriver.Edge(service=service)  # Membuka browser Edge menggunakan service yang telah dikonfigurasi

# 5. Akses situs Bing
driver.get("https://www.bing.com")  # Mengarahkan browser untuk membuka halaman Bing

# 6. Baca kata kunci dari file teks
# Program akan membuka file yang berisi daftar kata kunci yang akan digunakan untuk pencarian.
with open(keywords_file, "r") as file:
    keywords = file.readlines()  # Membaca semua baris dalam file dan menyimpannya sebagai list

# 7. Melakukan pencarian untuk setiap kata kunci dalam daftar
# Loop ini akan menjalankan pencarian untuk setiap kata kunci yang ada di dalam file.
for keyword in keywords:
    search_box = driver.find_element("name", "q")  # Menemukan elemen pencarian dengan atribut "name" yang bernama "q"
    search_box.clear()  # Menghapus teks yang ada di kotak pencarian sebelumnya, jika ada
    search_box.send_keys(keyword.strip())  # Memasukkan kata kunci ke dalam kotak pencarian
    search_box.send_keys(Keys.RETURN)  # Menekan tombol "Enter" untuk menjalankan pencarian

    time.sleep(2)  # Menunggu 2 detik agar hasil pencarian dapat muncul sebelum melakukan pencarian berikutnya

# 8. Menutup browser setelah selesai
driver.quit()  # Menutup browser setelah semua pencarian selesai
