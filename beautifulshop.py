import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

# URL yang ingin di-scrape
url = 'https://www.kompas.com/global/read/2025/04/09/123149070/china-akan-larang-semua-film-dari-as-balas-tarif-impor-104-persen-trump'

# Mengirim permintaan GET ke URL
response = requests.get(url)

# Memeriksa apakah permintaan berhasil
if response.status_code == 200:
    # Membuat objek BeautifulSoup dari konten HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    # Mengambil judul artikel
    content_title = soup.find('h1').text  # Menyimpan judul

    # Mencoba mengambil tanggal publikasi
    content_published_date = soup.find('meta', property='article:published_time')
    if content_published_date:
        # Mengambil konten dan mengonversi ke objek datetime
        utc_time = datetime.fromisoformat(content_published_date['content'].replace('Z', '+00:00'))
        
        # Mengonversi ke zona waktu WIB
        wib_time = utc_time.astimezone(pytz.timezone('Asia/Jakarta'))
        published_date = wib_time.strftime('%d/%m/%Y, %H:%M WIB')  # Format yang diinginkan
    else:
        published_date = "Tanggal publikasi tidak ditemukan"

    # Mengambil tag
    content_tags = soup.find('meta', {'name': 'keywords'})
    if content_tags:
        tags = content_tags['content']  # Mengambil tag dari tag meta
    else:
        tags = "Tag tidak ditemukan"

    # Menampilkan hasil
    print("Judul Artikel:", content_title)
    print("Tanggal Publikasi:", published_date)
    print("Tag:", tags)

else:
    print(f'Gagal mengakses URL. Kode status: {response.status_code}')