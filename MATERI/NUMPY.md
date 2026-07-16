(Numerical Python)
NumPy, singkatan dari Numerical Python, adalah salah satu pustaka inti dalam ekosistem Python yang dirancang untuk mendukung komputasi numerik secara efisien. Dengan fokus pada pengolahan Array multidimensi dan fungsi matematika yang kaya, NumPy menjadi dasar bagi banyak pustaka lain seperti Pandas, SciPy, TensorFlow, dan Matplotlib. Artikel ini akan membahas konsep-konsep dasar NumPy secara sistematis, mulai dari definisi hingga contoh aplikasi praktis.

1. Pengenalan Numpy
Apa itu NumPy?
NumPy adalah pustaka sumber terbuka untuk komputasi numerik berperforma tinggi di Python. Fitur utamanya adalah objek ndarray (N-dimensional array) untuk menyimpan elemen homogen secara efisien.

Mengapa Menggunakan NumPy?


Performa Tinggi: Implementasi NumPy dioptimalkan menggunakan bahasa C, sehingga jauh lebih cepat daripada daftar (list) Python.

Efisiensi Memori: NumPy menghemat memori dengan menegakkan homogenitas tipe data.

Fungsionalitas Kaya: Menyediakan fungsi bawaan untuk operasi matematika, statistik, dan aljabar linear.

Keterpaduan dengan Pustaka Lain: Mudah diintegrasikan dengan pustaka ilmiah lainnya.


Instalasi dan Impor NumPy:

Untuk menggunakan NumPy, Anda perlu menginstalnya terlebih dahulu melalui pip:

pip install numpy
Setelah instalasi, impor pustaka dengan alias konvensional np:

import numpy as np
2. Pembuatan Array dalam NumPy
Memahami Array NumPy:


Array NumPy adalah kumpulan nilai homogen yang disusun dalam grid, diindeks oleh tupel bilangan bulat non-negatif. Setiap Array memiliki atribut penting seperti:

.shape, .size, dan .dtype.

Contoh Atribut Array:

arr = np.array([[1, 2], [3, 4]])
print(arr.shape)  # (2, 2)
print(arr.size)   # 4
print(arr.dtype)  # int64
Membuat Array Menggunakan np.array:


Anda dapat membuat Array NumPy dari daftar atau tupel Python:

arr1 = np.array([1, 2, 3, 4])  # Array 1D
arr2 = np.array([[1, 2], [3, 4]])  # Array 2D
print(arr1)  # Output: [1 2 3 4]
print(arr2)  # Output: [[1 2] [3 4]]
Fungsi Khusus untuk Membuat Array:

np.zeros(): Array berisi nol.
zeros_array = np.zeros((3, 4))  # Array 3x4 berisi nol
print(zeros_array)
Output:
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
np.ones(): Array berisi satu.
ones_array = np.ones((2, 3))  # Array 2x3 berisi satu
print(ones_array)
Output:
[[1. 1. 1.]
 [1. 1. 1.]]
np.random.rand(): Array nilai acak antara 0-1.
random_array = np.random.rand(2, 3)  # Array 2x3 nilai acak
print(random_array)
np.arange(): Array dengan rentang nilai berurutan.
range_array = np.arange(0, 10, 2)  # Nilai dari 0 hingga 8 dengan langkah 2
print(range_array)  # Output: [0 2 4 6 8]
np.linspace(): Array nilai tersebar merata dalam interval.
linspace_array = np.linspace(0, 1, 5)  # 5 nilai dari 0 hingga 1
print(linspace_array)  # Output: [0.   0.25 0.5  0.75 1.  ]
3. Operasi Dasar pada Array NumPy
Operasi Aritmatika:

Operasi dilakukan secara elemen-demi-elemen (element-wise):

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # Output: [5 7 9]
print(a * b)  # Output: [4 10 18]
print(a - b)  # Output: [-3 -3 -3]
print(a / b)  # Output: [0.25 0.4  0.5 ]
Pengindeksan dan Irisan (Slicing)

Akses elemen Array menggunakan indeks:

arr = np.array([10, 20, 30, 40, 50])
print(arr[0])       # Output: 10
print(arr[1:4])     # Output: [20 30 40]
print(arr[-1])      # Output: 50 (elemen terakhir)
Mengubah Bentuk Array

Ubah dimensi Array tanpa mengubah data:

arr = np.arange(6)  # [0 1 2 3 4 5]
reshaped_arr = arr.reshape(2, 3)  # Ubah ke bentuk 2x3
print(reshaped_arr)
Output

[[0 1 2]
 [3 4 5]]
Penggabungan dan Penumpukan:

Gabungkan Array secara vertikal atau horizontal:

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

stacked = np.vstack((a, b))  # Penumpukan vertikal
print(stacked)
# Output:
# [[1 2 3]
#  [4 5 6]]

concatenated = np.concatenate((a, b))  # Horizontal concatenation
print(concatenated)  # Output: [1 2 3 4 5 6]
4. Fungsi Matematika dalam NumPy
Fungsi Statistik

Hitung statistik deskriptif:

arr = np.array([1, 2, 3, 4, 5])

median = np.median(arr)  # Median: 3
mean = np.mean(arr)      # Rata-rata: 3.0
std_dev = np.std(arr)    # Standar deviasi: ~1.414
total = np.sum(arr)      # Jumlah: 15

print(median, mean, std_dev, total)   
Fungsi Aljabar Linear

Lakukan perkalian matriks (matrix multiplication):

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

result = np.dot(a, b)  # Perkalian matriks
print(result)
# Output:
# [[19 22]
#  [43 50]]
5. Contoh Praktis dan Aplikasi
Simulasi Data Acak:

Hasilkan skor ujian acak:

scores = np.random.rand(5, 3) * 100  # Skala ke 0-100
print(scores)
# Contoh Output:
# [[23.4 56.7 89.1]
#  [12.3 45.6 78.9]
#  [34.5 67.8 90.1]
#  [45.6 78.9 12.3]
#  [56.7 89.1 23.4]]
Menghitung Median per Subjek:

Hitung median untuk setiap subjek:

subject_medians = np.median(scores, axis=0)
print(subject_medians)
# Contoh Output: [Median for each subject]
Perkalian Matriks Transformasi:

Kalikan matriks transformasi:

transformation1 = np.array([[1, 0], [0, -1]])
transformation2 = np.array([[0, -1], [1, 0]])

result = np.dot(transformation1, transformation2)
print(result)
# Output:
# [[ 0 -1]
#  [-1  0]]
6. Kesimpulan
NumPy adalah pustaka penting dalam analisis data dan komputasi numerik di Python, menawarkan performa tinggi, operasi array yang efisien, serta kompatibilitas luas dengan ekosistem ilmu data.


# Quick Note
Dalam pembelajaran mesin (machine learning), pustaka NumPy dan Pandas adalah alat yang sangat penting untuk manipulasi dan analisis data. Keduanya memiliki peran yang saling melengkapi: NumPy unggul dalam komputasi numerik berperforma tinggi pada Arrays, sementara Pandas menyediakan alat yang kuat untuk menangani data terstruktur, seperti tabel (dataframes).

NumPy : Operasi Arrays yang Efisien
NumPy menjadi fondasi bagi banyak aplikasi ilmiah dan pembelajaran mesin karena kemampuannya dalam mengelola Arrays multidimensi dengan efisien. Berikut adalah penjelasan rinci tentang cara membuat Arrays dan melakukan operasi pada Arrays tersebut.

1. Membuat Arrays
NumPy menyediakan berbagai fungsi untuk membuat Arrays dengan struktur dan tipe data yang berbeda. Berikut adalah contoh-contoh umum:

Contoh 1: Membuat Arrays Berisi Nol

import numpy as np

# Create a 3x3 array filled with zeros
zeros_array = np.zeros((3, 3))
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

# Create a 3x3 array of uniformly distributed random values
random_array = np.random.rand(3, 3)
# Example output:
# [[0.5488135  0.71518937 0.60276338]
#  [0.54488318 0.4236548  0.64589411]
#  [0.43758721 0.891773   0.96366276]]

    
2. Bekerja dengan Arrays
Setelah Arrays dibuat, Anda dapat melakukan berbagai operasi matematika dan statistik padanya. Berikut adalah beberapa operasi umum:

# Calculate the median value of the array
median_value = np.median(random_array)
# Example output: 0.60276338

# Compute the dot product (scalar product) with another array
b = np.random.rand(3)
# Example b: [0.60884455 0.93839021 0.22864655]
dot_product = np.dot(random_array, b)
# Example output: [1.14308858 0.87698413 1.32359181]

    
Kesimpulan
NumPy dioptimalkan untuk komputasi numerik berperforma tinggi.
Fungsi seperti np.zeros, np.random.rand, np.median, dan np.dot sangat berguna untuk berbagai operasi ilmiah dan statistik.
Kemampuan NumPy dalam menangani Arrays multidimensi menjadikannya dasar bagi pustaka lain seperti Pandas dan TensorFlow.