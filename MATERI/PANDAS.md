# Panduan Memulai Pandas

## 1. Pengenalan Pandas
Apa Itu Pandas?
Pandas adalah library Python yang sangat populer digunakan untuk analisis data terstruktur. Pandas menyediakan dua struktur utama:

Series: Struktur satu dimensi (mirip dengan array atau list) yang dapat menyimpan berbagai tipe data, termasuk numerik, string, atau objek lainnya.

DataFrame: Struktur dua dimensi (mirip tabel spreadsheet atau database) yang terdiri dari baris (rows) dan kolom (columns).

Pandas banyak digunakan karena kemampuannya dalam:

Membersihkan dataset yang kotor (menghapus duplikat, menangani nilai kosong, dll.).

Melakukan transformasi data seperti reshape, pivot, dan merge.

Menghitung statistik dasar (mean, median, std, dll.) dengan cepat.

Bekerja secara kompatibel dengan library lain seperti NumPy, Matplotlib, dan Scikit-learn.


Mengapa Harus Belajar Pandas?
Data Cleaning: Memperbaiki kesalahan, menangani nilai yang hilang (missing values), dan menghapus duplikat.

Transformasi Data: Mereset bentuk data agar lebih mudah dianalisis.

Statistik Cepat: Menghitung metrik seperti rata-rata (mean), total (sum), dan tren (trends).

Kompatibilitas: Integrasi dengan alat visualisasi (Matplotlib/Seaborn) dan pembelajaran mesin (Scikit-learn).


Cara Instalasi Pandas
Gunakan perintah berikut di terminal atau command prompt:

pip install pandas
Cara Instalasi Pandas

import pandas as pd
## 2. Membuat, Mengimpor, dan Mengekspor DataFrame
Cara Instalasi Pandas
DataFrame dapat dibuat dari berbagai sumber, seperti list, dictionary, file CSV, Excel, atau database.

Contoh: Membuat DataFrame dari Dictionary

Berikut cara membuat DataFrame menggunakan dictionary:

data = {
    'Nama': ['Alice', 'Bob', 'Charlie'],
    'Umur': [25, 30, 35],
    'Kota': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
Output:

    Nama  Umur         Kota
0   Alice    25     New York
1     Bob    30  Los Angeles
2 Charlie    35      Chicago

DataFrame ini memiliki tiga kolom: "Nama", "Umur", dan "Kota". Setiap baris mewakili individu dengan detailnya.



Memuat Data dari File

Pandas menyediakan fungsi praktis untuk membaca data dari berbagai format file:

CSV: pd.read_csv('filename.csv')

Excel: pd.read_excel('filename.xlsx')

JSON: pd.read_json('filename.json')

Contoh: Memuat File CSV

df = pd.read_csv('data.csv')
print(df.head())  # Menampilkan lima baris pertama
Fungsi .head() berguna untuk melihat sekilas dataset tanpa mencetak semua baris.



Menyimpan Data ke File
Anda juga dapat menyimpan DataFrame ke berbagai format:

CSV: df.to_csv('output.csv', index=False)

Excel: df.to_excel('output.xlsx', index=False)

Opsi index=False mencegah Pandas menambahkan nomor indeks ke file output.

## 3. Mengakses dan Memodifikasi Data
Menggunakan Indeks
Setiap baris dalam DataFrame memiliki indeks, yang bisa disesuaikan. Secara default, Pandas memberikan indeks numerik mulai dari 0. Anda dapat menetapkan kolom tertentu sebagai indeks menggunakan .set_index().

Contoh: Menetapkan Kolom sebagai Indeks

df.set_index('Nama', inplace=True)
print(df)
Output

         Umur         Kota
Nama
Alice      25     New York
Bob        30  Los Angeles
Charlie    35      Chicago
Memilih Data
Anda dapat mengambil data spesifik menggunakan:

Pemilihan Kolom: df['NamaKolom']

Pemilihan Baris: df.loc[label] atau df.iloc[index]

Penyaringan Kondisional: df[df['NamaKolom'] > nilai]

Contoh: Penyaringan Kondisional

  filtered_df = df[df['Umur'] > 30]
print(filtered_df)
Ini hanya akan mengembalikan baris di mana kolom "Umur" lebih besar dari 30.


Menambah atau Memodifikasi Data
Tambahkan kolom baru atau modifikasi kolom yang ada:

  filtered_df = df[df['Umur'] > 30]
print(filtered_df)
Ini menambahkan kolom baru bernama "Gaji".

# 2. Membuat, Membaca, dan Menulis
## 1. Pendahuluan
Dalam bidang ilmu data, bekerja dengan dataset adalah keterampilan mendasar yang harus dikuasai. Baik Anda menganalisis tren, membangun model Machine Learning, atau membuat visualisasi, pemahaman tentang cara membuat (Creating), membaca (Reading), dan menulis (Writing) data sangatlah penting. Panduan ini akan membimbing Anda melalui proses-proses tersebut langkah demi langkah menggunakan pustaka pandas di Python. Setelah selesai membaca panduan ini, Anda akan memiliki pengetahuan yang cukup untuk menangani data secara efisien dalam proyek Anda.

## 2. Menyiapkan Lingkungan Kerja
Sebelum mempelajari konsep inti, pastikan Anda telah menginstal alat-alat yang diperlukan:
Python: Instal dari python.org.
Pandas: Instal menggunakan:
pip  install pandas
Jupyter Notebook (Opsional):
pip  install notebook
Import Library:

  import  pandas  as pd
Alias pd adalah konvensi yang diterima secara luas di komunitas ilmu data.

## 3. Konsep Inti dalam Pandas
DataFrame: adalah struktur data dua dimensi dalam pandas. Ini terdiri dari baris dan kolom, mirip dengan spreadsheet atau tabel SQL. Setiap kolom dapat menyimpan data dengan tipe berbeda (misalnya, bilangan bulat, string, float).

Contoh: Membuat DataFrame

data = {
    "Nama": ["Ani", "Budi", "Citra"],
    "Usia": [25, 30, 35],
    "Kota": ["Jakarta", "Bandung", "Surabaya"]
}
df = pd.DataFrame(data)
print(df)
Series:

usia_series = df["Usia"]
print(usia_series)
Index: adalah label untuk setiap baris dalam DataFrame atau Series. Secara default, pandas memberikan indeks numerik mulai dari 0. Namun, Anda dapat menyesuaikan indeks agar lebih bermakna.

df = pd.DataFrame(data, index=["Orang1", "Orang2", "Orang3"])
print(df)
read_csv: Fungsi read_csv ( ) digunakan untuk memuat data dari file CSV ke dalam DataFrame.

df = pd.read_csv("data.csv")
print(df)
shape dan head: Atribut shape mengembalikan dimensi DataFrame sebagai tuple (baris, kolom).

print(df.shape)
print(df.head(2))

## 4. Membaca File dari Direktori Berbeda
Path Absolut: Path absolut menentukan lokasi tepat file di sistem Anda.

```
file_path = "/home/user/Documents/data.csv"
df = pd. read_csv(file_path)
print (df. head())
```

Path Relatif: Path relatif ditentukan relatif terhadap direktori kerja saat ini dari skrip atau notebook Anda.

Contoh: Struktur Direktori Proyek :

file_path = "../data/data.csv"
df = pd.read_csv(file_path)
print(df.head())
Mengubah Direktori Kerja: Gunakan modul os untuk mengubah direktori kerja.

import os
os.chdir("/path/to/your/directory")
df = pd.read_csv("data.csv")
print(df.head())
Variabel Lingkungan untuk Path Dinamis: Gunakan variabel lingkungan untuk menentukan path secara dinamis.

import os
data_directory = os.getenv("DATA_DIR", "/default/path/to/data")
file_path = os.path.join(data_directory, "data.csv")
df = pd.read_csv(file_path)
print(df.head())
Membaca File dari URL: Anda dapat membaca file langsung dari URL.

url = "https://example.com/data.csv"
df = pd.read_csv(url)
print(df.head())
Memecahkan Masalah Umum:

File Tidak Ditemukan: Periksa path file.
Izin Ditolak: Cek izin baca file.
Kesalahan Encoding: Gunakan:
df = pd.read_csv("data.csv", encoding="utf-8")

## 5. Contoh Praktis: Menggabungkan Konsep
Langkah 1: Membuat DataFrame: Mari kita gabungkan semua konsep yang telah dibahas ke dalam contoh praktis.

data  = {
    "Produk":[ "Laptop", "Smartphone", "Tablet"],
    "Harga" :[ 1200, 800, 400],
    "Stok"  :[ 15, 50, 20]
}
df = pd.DataFrame(data, index=["Barang1", "Barang2", "Barang3"])
print(df)
Langkah 2: Mengakses Series:

harga_series = df["Harga"]
print(harga_series)
Langkah 3: Memeriksa Dimensi:

print(df.shape)
Langkah 4: Memeriksa Beberapa Baris Pertama:

print(df.head(2))
## 6. Poin Penting
DataFrame: Struktur tabular dua dimensi.
Series: Array satu dimensi, kolom tunggal.
Index: Label baris yang dapat disesuaikan.
Fungsi read_csv() Memuat data CSV ke DataFrame.
Atribut shape Memberikan dimensi DataFrame.
Metode head(): Menampilkan baris awal DataFrame.

# 3. Indeksasi, Pemilihan, dan Penugasan
## 1. Pendahuluan
Apa Itu Pandas?
Pandas adalah pustaka Python open-source yang banyak digunakan untuk manipulasi dan analisis data. Pandas menyediakan alat kuat untuk menangani data terstruktur, seperti tabel (mirip dengan spreadsheet atau basis data SQL). Di inti Pandas, terdapat dua struktur data utama: Series dan DataFrame.

Struktur Data Inti di Pandas:

Series: Struktur satu dimensi mirip array dengan indeks berlabel. Bayangkan ini sebagai kolom tunggal dalam spreadsheet.
DataFrame: Struktur dua dimensi mirip tabel yang terdiri dari baris dan kolom. Setiap kolom dalam DataFrame pada dasarnya adalah sebuah Series, membentuk dataset tabular yang dapat dimanipulasi secara efisien.

## 2. Memahami Pengindeksan (Indexing)
Apa Itu Pengindeksan?
Pengindeksan merujuk pada akses ke elemen, baris, atau kolom tertentu dalam DataFrame atau Series Pandas. Ini mirip dengan navigasi melalui baris dan kolom dalam spreadsheet untuk mengekstrak informasi yang tepat.

Jenis-Jenis Pengindeksan:

Pengindeksan Berbasis Label (.loc[]):
import pandas as pd
data = {'Nama': ['Ani', 'Budi', 'Citra'], 'Usia': [25, 30, 35]}
df = pd.DataFrame(data, index=['A', 'B', 'C'])
print(df.loc['B', 'Usia'])  # Output: 30
Pengindeksan Berbasis Posisi (.iloc[]):
print(df.iloc[1, 0])  # Output: Budi
Pengindeksan Campuran:  Menggabungkan pengindeksan berbasis label dan posisi.
print(df.iloc[:2].loc[:, 'Nama'])

## 3. Memilih Data (Selecting)
Memilih Kolom: Anda dapat memilih satu atau lebih kolom dengan memberikan nama mereka sebagai kunci.

usia = df['Usia']
subset = df[['Nama', 'Usia']]
Pemilihan Kondisional:

filtered = df[df['Usia'] > 30]
Menggabungkan Kondisi:

filtered = df[(df['Usia'] > 25) & (df['Nama'].str.startswith('A'))]
Menggunakan .notnull():

filtered = df[df['Usia'].notnull()]

## 4. Menetapkan Nilai (Assigning)
Memodifikasi Nilai yang Ada:

df.loc['B', 'Usia'] = 32
Menambahkan Kolom Baru:

df['Kota'] = ['Jakarta', 'Bandung', 'Surabaya']
Mengganti Nilai:

df['Kota'] = df['Kota'].replace('Jakarta', 'JKT')
Menetapkan Ulang Indeks:

df = df.set_index('Nama')
Membalik Urutan Baris:

df = df.iloc[::-1].reset_index(drop=True)

## 5. Teknik Lanjutan
Menggunakan .query() untuk Pemilihan:

filtered = df.query('Usia > 30')
MultiIndexing / MultiIndeksasi:

arrays = [['A', 'A', 'B', 'B'], [1, 2, 1, 2]]
index = pd.MultiIndex.from_arrays(arrays, names=('Huruf', 'Nomor'))
df_multi = pd.DataFrame({'Nilai': [10, 20, 30, 40]}, index=index)
print(df_multi)

## 6. Praktik Terbaik
Gunakan .loc[] dan .iloc[] untuk pengindeksan yang jelas.
Gunakan label yang deskriptif untuk kolom dan indeks.
Manfaatkan operasi vektorisasi untuk efisiensi.
Selalu tangani nilai kosong (missing values).

## 7. Poin Penting
Pahami Series dan DataFrame.
Gunakan pengindeksan berbasis label (.loc[]) dan posisi (.iloc[]).
Filter data menggunakan kondisi logis.
Modifikasi dan tambah data dengan metode Pandas.
Eksplorasi teknik lanjutan seperti query dan MultiIndexing.
Ikuti praktik terbaik untuk efisiensi dan keterbacaan.


# 4. Summary Functions dan Maps
## 1. Pendahuluan
1.1 Apa Itu Fungsi Ringkasan (Summary Functions)?
Fungsi ringkasan adalah metode yang telah ditentukan sebelumnya dalam pustaka seperti Pandas yang membantu merangkum atau menggabungkan data. Fungsi ini memberikan wawasan cepat tentang karakteristik dataset, seperti rata-rata (mean), total (sum), rentang (range), dan distribusi. Fungsi-fungsi ini sangat penting dalam Exploratory Data Analysis (EDA) karena memungkinkan kita memahami data dengan sekilas.

## 1.2 Apa Itu Pemetaan (Maps)?
Dalam analisis data, "pemetaan" merujuk pada operasi yang menerapkan fungsi atau transformasi ke setiap elemen dalam dataset. Pemetaan memungkinkan kita memodifikasi atau meningkatkan data secara sistematis, membuatnya lebih cocok untuk analisis atau visualisasi.

## 2. Memahami Fungsi Ringkasan
Fungsi Ringkasan yang Umum Digunakan:

describe(): Fungsi describe() menghasilkan ringkasan statistik dari kolom numerik dalam dataset. Ini memberikan metrik seperti jumlah (count), rata-rata (mean), standar deviasi (std), minimum (min), maksimum (max), dan nilai kuartil.
import pandas as pd
df = pd.read_csv('data.csv')
print(df.describe())
mean(): Fungsi mean() menghitung nilai rata-rata dari sebuah kolom. Ini sangat berguna untuk memahami kecenderungan pusat dalam data numerik.
average_value = df['column_name'].mean()
print(f"Nilai rata-rata: {average_value}")
sum(): Fungsi sum() menghitung total semua nilai dalam sebuah kolom. Ini berguna untuk analisis keuangan atau data kumulatif..
total_sales = df['sales'].sum()
print(f"Total penjualan: {total_sales}")
min() dan max(): Mencari nilai minimum dan maksimum.
lowest = df['temperature'].min()
highest = df['temperature'].max()
value_counts(): Menghitung frekuensi nilai unik.
category_counts = df['category'].value_counts()
unique(): Menampilkan nilai unik.
unique_categories = df['category'].unique()
head(): Menampilkan beberapa baris pertama.
print(df.head())

## 3. Menjelajahi Pemetaan (Maps) dalam Transformasi Data
Jenis-Jenis Pemetaan:

map(): Fungsi map() menerapkan transformasi ke setiap elemen dalam Series. Ini sering digunakan untuk transformasi sederhana, seperti mengonversi unit atau mengkodekan variabel kategorikal.
df['temperature_f'] = df['temperature_c'].map(lambda x: (x * 9/5) + 32)
apply(): Fungsi apply() lebih fleksibel daripada map(). Ini dapat diterapkan ke baris dan kolom DataFrame, serta mendukung operasi yang lebih kompleks.
df['difference'] = df.apply(lambda row: row['value_a'] - rrow['value_b'], axis=1)
Fungsi Kustom dengan map(): Anda dapat mendefinisikan fungsi kustom dan menggunakannya dengan map() atau apply() untuk melakukan transformasi yang disesuaikan.
def categorize_age(age):
    if age < 18:
        return 'Minor'
    elif 18 <= age <= 65:
        return 'Adult'
    else:
        return 'Senior'

df['age_category'] = df['age'].map(categorize_age)

## 4. Menggabungkan Fungsi Ringkasan dan Pemetaan
Contoh Alur Kerja:

Muat dataset dengan read_csv().
Gunakan map() atau apply() untuk membuat fitur turunan.
Analisis fitur baru menggunakan value_counts() dan groupby().
import pandas as pd

df = pd.read_csv('data.csv')
df['price_category'] = df['price'].map(lambda x: 'High' if x > 100 else 'Low')

print(df['price_category'].value_counts ())
print(df.groupby('price_category')['sales'].mean())


## 5. Aplikasi Praktis
Studi Kasus 1: Analisis Penjualan Ritel

Bayangkan Anda sedang menganalisis data penjualan untuk perusahaan ritel. Anda dapat menggunakan fungsi ringkasan untuk menghitung total pendapatan dan nilai pesanan rata-rata. Kemudian, gunakan pemetaan untuk mengkategorikan pelanggan berdasarkan kebiasaan belanja mereka.

Identifikasi kategori produk unik dengan unique().
Periksa beberapa baris pertama dengan head().
unique_categories = df['product_category'].unique()
print(unique_categories)

print(df.head())
Studi Kasus 2: Eksplorasi Data Iklim

Untuk data iklim, Anda mungkin menggunakan fungsi ringkasan untuk menentukan suhu rata-rata selama periode tertentu. Pemetaan dapat membantu mengonversi skala suhu atau mengklasifikasikan hari sebagai "panas," "sedang," atau "dingin."

Periksa kondisi cuaca unik dengan unique().
Lihat pratinjau dataset dengan head().
unique_conditions = df['weather_condition'].unique()
print(unique_conditions)

print(df.head())

# 5. Pengelompokkan dan Pengurutan

## 1. Pendahuluan Grouping
Apa Itu Pengelompokan (Grouping)?
Pengelompokan merujuk pada proses membagi dataset menjadi subset berdasarkan satu atau lebih variabel kategorikal. Setiap subset sesuai dengan kombinasi unik nilai dari kolom pengelompokan yang ditentukan. Setelah dikelompokkan, Anda dapat melakukan operasi agregasi (misalnya, jumlah, rata-rata, hitungan) pada setiap subset untuk mengekstrak statistik ringkasan.

Sebagai contoh, jika Anda memiliki dataset transaksi penjualan, Anda mungkin mengelompokkan data berdasarkan "wilayah" dan "kategori produk" untuk menghitung total penjualan untuk setiap kombinasi variabel tersebut.

Mengapa Pengelompokan Penting?

Ringkasan Data Pengelompokan memungkinkan Anda menyusutkan dataset besar menjadi ringkasan yang mudah dikelola.
Identifikasi Pola Dengan menggabungkan data, Anda dapat mengungkap tren dan hubungan dalam kelompok tertentu.
Perbandingan antar Segmen Pengelompokan memungkinkan Anda membandingkan metrik di berbagai kategori atau segmen.
Implementasi di Python (Menggunakan Pandas): 

Pustaka pandas di Python menyediakan metode kuat bernama .groupby() untuk melakukan operasi pengelompokan. Berikut adalah penjelasan langkah demi langkah tentang cara menggunakannya

Langkah 1: Impor Pustaka yang DiperlukanLangkah 
Langkah 2: Muat Dataset Anda
Langkah 3: Lakukan Pengelompokan dengan Agregasi

import pandas as pd
df = pd.read_csv ('sales_data.csv')

grouped = df.groupby('Wilayah')['Penjualan'].agg(['sum', 'mean'])
print(grouped)
Pengelompokan Multi-Level: Anda juga dapat mengelompokkan berdasarkan beberapa kolom. Misalnya, untuk mengelompokkan berdasarkan Wilayah dan Kategori Produk:

multi_grouped = df.groupby(['Wilayah', 'Kategori_Produk'])['Penjualan'].agg(['sum', 'mean'])
print(multi_grouped)
Reset Index: Secara default, .groupby() menghasilkan indeks hierarkis. Untuk mengonversinya kembali ke DataFrame standar, gunakan .reset_index():

reset_grouped = multi_grouped.reset_index()
print(reset_grouped)

## 2. Pengurutan (Sorting) dalam Analisis Data
Apa Itu Pengurutan?
Pengurutan melibatkan pengaturan baris dataset dalam urutan tertentu berdasarkan satu atau lebih kolom. Operasi ini sangat berguna untuk memprioritaskan titik data, mengidentifikasi ekstrem (misalnya, nilai tertinggi atau terendah), atau sekadar membuat dataset lebih mudah dibaca. 

Mengapa Pengurutan Penting?

Organisasi Data: Pengurutan membantu mengorganisasi data secara logis, sehingga lebih mudah dianalisis.

Menyoroti Ekstrem: Anda dapat dengan cepat mengidentifikasi entri teratas atau bawah dalam dataset.

Persiapan Visualisasi: Data yang diurutkan sering kali menjadi dasar untuk membuat visualisasi yang efektif.

Implementasi di Python (Menggunakan Pandas):

Langkah 1: Pengurutan Dasar: 

Untuk mengurutkan dataset berdasarkan kolom Penjualan dalam urutan menurun:

sorted_df = df.sort_values(by='Penjualan', ascending=False)
print(sorted_df)
Langkah 2: Pengurutan Berdasarkan Beberapa Kolom:


Jika Anda ingin mengurutkan berdasarkan beberapa kolom (misalnya, pertama berdasarkan Wilayah dalam urutan naik dan kemudian berdasarkan Penjualan dalam urutan turun):

multi_sorted = df.sort_values(by=['Wilayah', 'Penjualan'], ascending=[True, False])
print (multi_sorted)
Langkah 3: Pengurutan Setelah Pengelompokan:

Setelah melakukan operasi pengelompokan, Anda dapat mengurutkan ringkasan yang dihasilkan. Sebagai contoh, untuk mengurutkan data penjualan berdasarkan total penjualan dalam urutan menurun:

grouped = df.groupby('Wilayah')['Penjualan'].sum()
sorted_grouped = grouped.sort_values(ascending=False)
print(sorted_grouped)

## 3. Menggabungkan Pengelompokan dan Pengurutan
Contoh: 5 Wilayah Teratas Berdasarkan Total Penjualan

Berikut cara menggabungkan pengelompokan dan pengurutan untuk mengidentifikasi wilayah dengan kinerja terbaik:

grouped_sales = df.groupby('Wilayah')['Penjualan'].agg(['sum'])
sorted_sales = grouped_sales.sort_values (by='sum', ascending=False)
top_regions = sorted_sales.head(5)
print(top_regions)
Interpretasi Output:
Output akan menunjukkan 5 wilayah dengan total penjualan tertinggi, memungkinkan Anda memfokuskan analisis pada area kunci ini.

## 4. Fungsi Utama dan Peran Mereka
.agg(): Fungsi .agg() digunakan untuk menerapkan beberapa operasi agregasi (misalnya, sum, mean, count) ke data yang dikelompokkan. Ini memberikan fleksibilitas dalam merangkum data. Contohnya:
grouped = df.groupby('Wilayah')['Penjualan'].agg({
    'Total_Penjualan': 'sum',
    'Rata_Rata_Penjualan': 'mean',
    'Jumlah_Transaksi': 'count'
})
print(grouped)
Indeks: Saat Anda mengelompokkan data, kolom pengelompokan menjadi bagian dari indeks. Struktur hierarkis ini dapat berguna untuk operasi tertentu tetapi mungkin perlu diratakan untuk operasi lainnya.
reset_index(): Mengonversi indeks hierarkis kembali ke format DataFrame standar:
reset_grouped = grouped.reset_index()
print(reset_grouped)
Fungsi .sort_values() mengurutkan baris berdasarkan satu atau lebih kolom. Ini mendukung baik urutan naik maupun turun dan dapat menangani ikatan menggunakan kriteria pengurutan sekunder:
sorted_df = df.sort_values(by=['Wilayah', 'Penjualan'], ascending=[True, False])
print(sorted_df)
sort_index(): Mengurutkan berdasarkan indeks (baik single maupun multi-level).
Contoh .sort_index():

grouped = df.groupby(['Wilayah', 'Kategori_Produk'])['Penjualan'].sum()
sorted_index = grouped.sort_index()
print(sorted_index)

## 5. Praktik Terbaik dan Tips
Pilih Kolom Relevan: Pilih kolom pengelompokan yang logis untuk tujuan analisis.
Gunakan Beragam Agregasi: Tidak hanya menggunakan sum(), gunakan juga mean() atau count() bila perlu.
Tangani Nilai Hilang: Pastikan dataset bersih sebelum pengelompokan atau pengurutan.
Visualisasikan: Gunakan diagram batang, pie chart, atau heatmap untuk menyajikan hasil dengan lebih baik.
Optimasi Performa: Seleksi hanya kolom yang dibutuhkan untuk mengurangi beban komputasi pada dataset besar.


# 6. Tipe Data dan Nilai yang Hilang
1. Pendahuluan
Mengapa Memahami Tipe Data?
Dalam analisis data, memahami tipe data yang Anda kerjakan adalah fundamental. Tipe data menentukan bagaimana kita menginterpretasi, memproses, dan menganalisis informasi. Asumsi yang salah tentang tipe data dapat menyebabkan analisis yang keliru, visualisasi yang menyesatkan, dan kesimpulan yang tidak akurat. Misalnya, memperlakukan data kategorikal sebagai numerik (atau sebaliknya) dapat mengakibatkan metode statistik yang tidak sesuai diterapkan.

Tantangan Nilai Hilang:
Nilai hilang adalah masalah umum dalam dataset dunia nyata. Mereka muncul karena berbagai alasan seperti kesalahan manusia, pengumpulan data yang tidak lengkap, atau kegagalan sistem. Mengabaikan nilai hilang atau menanganinya secara tidak tepat dapat menyebabkan hasil yang bias dan mengurangi keandalan analisis Anda. Oleh karena itu, penting untuk mengidentifikasi dan menangani nilai hilang secara sistematis.

2. Memahami Tipe Data
Data Kategorikal vs. Numerik:

Kategorikal:
Jenis data ini merepresentasikan karakteristik atau label. Data ini tidak memiliki urutan alami atau makna numerik. Contohnya termasuk jenis kelamin (laki-laki/perempuan), kategori produk (elektronik, pakaian), atau kota (New York, London).
Numerik: Jenis data ini terdiri dari angka yang merepresentasikan kuantitas. Data numerik dapat dibagi lebih lanjut menjadi:
Data Diskrit: Nilai yang dapat dihitung dan terbatas, seperti jumlah siswa dalam sebuah kelas.
Data Kontinu: Nilai yang dapat mengambil nilai apa pun dalam rentang tertentu, seperti suhu atau berat badan.
Subtipe Data Kategorikal dan Numerik:

Data Kategorikal:
Nominal: Kategori tanpa urutan inheren (misalnya, warna: merah, biru, hijau).
Ordinal: Kategori dengan urutan bermakna (misalnya, tingkat pendidikan: SMA, sarjana, magister, doktor).
Data Numerik:
Integer: Bilangan bulat (misalnya, jumlah mobil yang terjual).
Float: Bilangan dengan titik desimal (misalnya, rata-rata pendapatan).
Contoh Praktis: ID Karyawan (kategorikal), Usia (numerik diskrit), Gaji (numerik kontinu), Departemen (kategorikal). 
Pertimbangkan dataset yang berisi informasi tentang karyawan:

ID Karyawan	Jenis Kelamin	Usia	Gaji ($)	Departemen
1	Laki-laki	30	50000.0	Teknik
2	Perempuan	25	60000.0	Pemasaran
3	Laki-laki	-	55000.0	Penjualan

ID Karyawan: Kategorikal (nominal)

Jenis Kelamin: Kategorikal (nominal)

Usia: Numerik (diskrit)

Gaji ($): Numerik (kontinu)

Departemen: Kategorikal (nominal)

Menggunakan dtype dan dtypes:


Fungsi dtype dan dtypes di Pandas adalah alat yang ampuh untuk memeriksa tipe data kolom dalam DataFrame. Fungsi-fungsi ini membantu Anda memahami bagaimana setiap kolom ditafsirkan oleh Python, memastikan bahwa analisis Anda sesuai dengan tipe data yang dimaksudkan.

Periksa Tipe Data Menggunakan dtypes
Periksa Tipe Data Kolom Tertentu Menggunakan dtype
Ubah Tipe Data
Menangani Tipe Data Campuran
Periksa Perubahan Setelah Konversi
import pandas as pd
df = pd.read_csv("data.csv")
print(df.dtypes)  # Memeriksa tipe semua kolom
print(df['Usia'].dtype)  # Tipe kolom spesifik
df['Usia'] = df['Usia'].astype(float)  # Konversi tipe data
df = df.convert_dtypes()  # Konversi otomatis tipe data terbaik
3. Menangani Nilai Hilang
Identifikasi Nilai Hilang:

Nilai hilang dapat muncul dalam berbagai bentuk, seperti sel kosong, placeholder seperti "NA" atau "NaN," atau bahkan entri yang salah seperti "-". Mengidentifikasi nilai-nilai ini adalah langkah pertama untuk menanganinya.

print(df.isnull().sum())  # Hitung jumlah nilai hilang
Strategi Penanganan:

Penghapusan: Hapus baris/kolom yang mengandung nilai hilang.
Imputasi: Ganti dengan mean/median/mode atau metode lainnya.
Flagging: Tandai nilai hilang dengan kolom tambahan.
Contoh Mengisi Nilai Hilang: 

Saat menangani data kategorikal, mengganti nilai hilang dengan placeholder seperti "Unknown" dapat menjadi strategi yang efektif. Pendekatan ini mempertahankan baris sambil jelas menandai bahwa nilai tersebut hilang.

# Untuk kolom kategorikal
df['Departemen'] = df['Departemen'].fillna('Unknown')

# Untuk semua kolom kategorikal
categorical_columns = df.select_dtypes(include=['object']).columns
df[categorical_columns] = df[categorical_columns].fillna('Unknown')

# Untuk kolom numerik
df['Usia'].fillna(df['Usia'].mean(), inplace=True)
Membersihkan Placeholder:

df.replace(['NA', '?', '-'], pd.NA, inplace=True)
4. Implementasi Praktis Menggunakan Python
Alat dan Pustaka untuk Analisis Data 
Python menawarkan pustaka kuat untuk analisis data, termasuk: 
Pandas: Untuk manipulasi dan analisis data.
# Muat data
import pandas as pd
df = pd.read_csv("data.csv")

# Cek tipe data
print(df.dtypes)

# Ubah tipe data jika perlu
df['Usia'] = df['Usia'].astype(float)
df['ID Karyawan'] = df['ID Karyawan'].astype(str)
df['ID Karyawan'] = df['ID Karyawan'].astype(str)
df = df.convert_dtypes()

# Identifikasi nilai hilang
print(df.isnull().sum())

# Ganti placeholder
df.replace(['NA', '?', '-'], pd.NA, inplace=True)

# Isi nilai kosong
categorical_columns = df.select_dtypes(include=['object']).columns
df[categorical_columns] = df[categorical_columns].fillna('Unknown')
df['Usia'].fillna(df['Usia'].mean(), inplace=True)
5. Poin Penting
Tipe data sangat penting untuk analisis dan interpretasi yang akurat. Gunakan dtype dan dtypes untuk memeriksa dan mengubah tipe data jika diperlukan.

Nilai hilang harus ditangani dengan hati-hati untuk menghindari bias dan menjaga integritas data. Gunakan fillna('Unknown') untuk data kategorikal dan replace() untuk membersihkan placeholder.

Pandas menyediakan alat yang kuat untuk mengelola tipe data dan nilai hilang.

Saat bekerja dengan dataset, selalu:

Inspeksi dan pahami tipe data menggunakan dtype dan dtypes.

Identifikasi dan tangani nilai hilang secara sistematis menggunakan fillna() dan replace().

Pilih metode yang sesuai dengan tujuan analisis Anda dan sifat data Anda


# 7. Penamaan dan Penggabungan
1. Mengganti Nama (Renaming) Kolom dalam DataFrame
Mengapa Mengganti Nama Kolom?
Mengganti nama kolom meningkatkan keterbacaan, konsistensi, dan membuat analisis lebih mudah dipahami.

Metode untuk Mengganti Nama Kolom
Menggunakan Metode rename():

import pandas as pd
data = {"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}
df = pd.DataFrame(data)
df.rename(columns={"A": "Alpha", "B": "Beta"}, inplace=True)
print(df)
Menggunakan Atribut columns:

df.columns = ["Alpha", "Beta", "Gamma"]
print(df)
Contoh Praktis:

data = {"f1": [25, 30, 35], "f2": [50000, 60000, 70000], "f3": ["L", "P", "L"]}
df = pd.DataFrame(data)
df.rename(columns={"f1": "Usia", "f2": "Pendapatan", "f3": "Jenis Kelamin"}, inplace=True)
print(df)
2. Menggabungkan (Combining) DataFrame
Mengapa Menggabungkan DataFrame?
Menggabungkan DataFrame menyatukan data dari berbagai sumber menjadi satu struktur tunggal yang koheren untuk analisis.

Jenis Penggabungan
Penyambungan (Concatenation):

df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
result = pd.concat([df1, df2], axis=0)
print(result)
Penggabungan (Merging):

df1 = pd.DataFrame({"Kunci": ["K1", "K2"], "A": [1, 2]})
df2 = pd.DataFrame({"Kunci": ["K1", "K2"], "B": [3, 4]})
result = pd.merge(df1, df2, on="Kunci", how="inner")
print(result)
Penyatuan (Joining):

df1 = pd.DataFrame({"A": [1, 2]}, index=["K1", "K2"])
df2 = pd.DataFrame({"B": [3, 4]}, index=["K1", "K2"])
result = df1.join(df2, how="inner")
print(result)
3. Praktik Terbaik untuk Mengganti Nama dan Menggabungkan DataFrame
Memastikan Konsistensi: Gunakan nama kolom yang deskriptif dan konsisten.
Menghindari Kesalahan: Periksa penggunaan inplace=True dan pastikan kecocokan kolom saat menggabungkan.
Tips Alur Kerja:
Gunakan nama kolom yang jelas sejak awal.
Uji penggabungan pada subset kecil sebelum seluruh dataset.
Dokumentasikan setiap langkah transformasi.


# Quick Note
1. Pengenalan Struktur Data Utama di Pandas
Dalam Pandas, manipulasi data berfokus pada dua struktur data inti:

DataFrame: Struktur dua dimensi, tabular (mirip dengan spreadsheet atau tabel SQL).
Series: Objek mirip array satu dimensi.
Anda dapat membuat DataFrame dari dictionary atau mengimpor data dari file CSV, lembar Excel, atau basis data.

2. Membuat DataFrame
import pandas as pd

# Inisialisasi DataFrame
data = {'A': [1, 2, None], 'B': [4, None, 6]}
df = pd.DataFrame(data)
print(df)
Output:

     A    B
0  1.0  4.0
1  2.0  NaN
2  NaN  6.0
3. Bekerja dengan DataFrame
Menghapus Nilai Hilang
Gunakan dropna() untuk menghapus baris yang memiliki nilai NaN:

cleaned_df = df.dropna()
print(cleaned_df)
Output:

     A    B
0  1.0  4.0
Mendapatkan Statistik Deskriptif
Gunakan describe() untuk mendapatkan ringkasan statistik:

description = df.describe()
print(description)
Output:

              A         B
count  2.000000  2.000000
mean   1.500000  5.000000
std    0.707107  1.414214
min    1.000000  4.000000
25%    1.250000  4.500000
50%    1.500000  5.000000
75%    1.750000  5.500000
max    2.000000  6.000000
Menggabungkan DataFrame
Gunakan pd.merge() untuk menggabungkan dua DataFrame berdasarkan kolom umum:

df2 = pd.DataFrame({'A': [1, 2, 3], 'C': [7, 8, 9]})
merged_df = pd.merge(df, df2, on='A')
print(merged_df)
Output:

     A    B  C
0  1.0  4.0  7
1  2.0  NaN  8
Mengelompokkan Data
Gunakan groupby() untuk mengelompokkan dan menghitung agregasi data:

grouped = df.groupby('A').sum()
print(grouped)
Output:

      B
A      
1.0  4.0
2.0  0.0
4. Poin Penting
DataFrame sangat serbaguna untuk manipulasi data terstruktur.
Operasi kunci: dropna(), describe(), merge(), groupby() wajib dikuasai.
Pastikan data bersih dan terstruktur sebelum melakukan analisis lanjutan.