# Panduan Menggunakan Scikit-learn

1. Pengantar
Mengapa Menggunakan Scikit-learn?
Scikit-learn adalah salah satu library paling populer untuk machine learning di Python karena beberapa alasan:

Sederhana: API-nya intuitif dengan sintaks yang konsisten (fit, predict, transform).
Komprehensif: Mendukung berbagai algoritma untuk klasifikasi, regresi, pengelompokan, dan reduksi dimensi.
Integrasi: Bekerja mulus dengan library lain seperti NumPy, pandas, dan Matplotlib.
Ekstensibilitas: Menyediakan alat untuk pra-pemrosesan data, evaluasi model, dan penyetelan hyperparameter.
Dukungan Komunitas: Didukung oleh komunitas open-source aktif dengan dokumentasi dan tutorial yang ekstensif.
Cara Menginstal Scikit-learn
Instal Python: Pastikan Python telah terinstal di sistem Anda. Anda dapat mengunduhnya dari (python.org).
Instal Dependensi: Scikit-learn membutuhkan NumPy dan SciPy. Instal menggunakan pip:
pip install numpy scipy
Instal Scikit-learn: Instal scikit-learn dengan perintah berikut:
pip install scikit-learn
Verifikasi Instalasi: Periksa versi scikit-learn untuk memastikan instalasi berhasil:
import sklearn
print(sklearn.__version__)
Opsional - Instal Library Visualisasi: Untuk visualisasi data, instal Matplotlib dan Seaborn:
pip install matplotlib seaborn



# 2. Pipeline Pemodelan Prediktif
2.1 Eksplorasi Data Tabular
Data tabular tersusun dalam baris (observasi) dan kolom (fitur). Memahami dataset adalah langkah penting sebelum membangun model. Ini melibatkan inspeksi distribusi data, identifikasi nilai yang hilang, dan eksplorasi hubungan antar fitur.

Langkah-Langkah Eksplorasi Data:

Muat dataset menggunakan pandas:
import pandas as pd
data = pd.read_csv('housing.csv')
Inspeksi lima baris pertama:
print(data.head())
Rangkuman statistik:
print(data.describe())
Periksa nilai yang hilang:
print(data.isnull().sum())
Studi Kasus: Dataset Harga Rumah California Tujuan: Jelajahi harga rumah dan identifikasi prediktor potensial seperti pendapatan median dan populasi.

Cara Menyelesaikan Studi Kasus

Memuat Dataset: Gunakan pandas untuk memuat dataset (housing.csv).
Memeriksa Data: Gunakan .head(), .describe(), dan .info() untuk memahami struktur dan statistik ringkasan.
Menangani Nilai yang Hilang: Identifikasi nilai yang hilang menggunakan .isnull().sum() dan imputasi nilai tersebut menggunakan mean, median, atau strategi lainnya.
Memvisualisasikan Hubungan: Gunakan seaborn.pairplot() atau sns.heatmap() untuk memvisualisasikan korelasi antara fitur dan variabel target (median_house_value).
Rekayasa Fitur: Buat fitur baru jika diperlukan (misalnya, menggabungkan latitude dan longitude menjadi satu fitur tunggal).
2.2 Melatih Model Scikit-learn pada Data Numerik
Pembelajaran terawasi melibatkan pelatihan model untuk memetakan input ke output. Untuk data numerik, model regresi sering digunakan. Scikit-learn menyediakan API yang konsisten (fit, predict) untuk pelatihan dan evaluasi model.

Langkah-Langkah Pelatihan Model Regresi Linear:

Persiapkan data:

X = data[['median_income']]  # Variabel prediktor
y = data['median_house_value']  # Variabel target
Pisahkan data menjadi set pelatihan dan pengujian:

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
Latih model:

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
Evaluasi model:

from sklearn.metrics import mean_squared_error

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
Studi Kasus: Dataset Harga Rumah Boston Tujuan: Prediksi harga rumah berdasarkan variabel seperti tingkat kejahatan dan jumlah kamar.

Cara Menyelesaikan Studi Kasus

Menyiapkan Fitur: Pilih fitur yang relevan (misalnya, CRIM, RM, AGE) dan variabel target (MEDV).
Membagi Data: Gunakan train_test_split untuk membagi data menjadi set pelatihan dan pengujian.
Melatih Model: Pasang model regresi linear menggunakan LinearRegression.
Mengevaluasi Model: Hitung metrik kinerja seperti Mean Squared Error (MSE) dan skor R².
Menginterpretasi Hasil: Analisis koefisien untuk memahami kepentingan fitu.

2.3 Penanganan Data Kategorikal
Variabel kategorikal harus diubah menjadi bentuk numerik agar dapat digunakan dalam algoritma ML. Teknik umum termasuk label encoding (untuk kategori ordinal) dan one-hot encoding (untuk kategori nominal).

Langkah-Langkah Encoding Data Kategorikal:

Identifikasi kolom kategorikal:

categorical_cols = ['ocean_proximity']
Buat pipeline pra-pemrosesan:

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_cols)
    ])
Integrasikan dengan model regresi:

from sklearn.pipeline import Pipeline

pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('regressor', LinearRegression())])
Latih dan evaluasi:

pipeline.fit(X_train, y_train)
score = pipeline.score(X_test, y_test)

print(f"R-squared: {score}")
Studi Kasus: Dataset Titanic Survival
Tujuan: Encode kelas penumpang (Pclass) dan pelabuhan keberangkatan (Embarked) untuk memprediksi probabilitas kelangsungan hidup.

Cara Menyelesaikan Studi Kasus

Mengidentifikasi Fitur Kategorikal: Identifikasi kolom kategorikal (Pclass, Embarked, dll.).
Mengkodekan Data Kategorikal: Gunakan OneHotEncoder atau LabelEncoder untuk mengkodekan variabel kategorikal.
Membangun Pipeline: Gabungkan langkah-langkah preprocessing dan classifier (misalnya, regresi logistik) dalam sebuah pipeline.
Melatih dan Mengevaluasi: Pasang pipeline pada data pelatihan dan evaluasi kinerja menggunakan akurasi atau ROC-AUC


# 3. Pemilihan Model Terbaik
3.1 Overfitting dan Underfitting
Overfitting terjadi ketika model terlalu kompleks dan belajar dari noise dalam data pelatihan, sedangkan underfitting terjadi ketika model terlalu sederhana untuk menangkap pola dasar. Visualisasi performa pada data pelatihan vs. data pengujian membantu mendiagnosis masalah ini.

Langkah-Langkah Visualisasi Performa:

1. Latih model pohon keputusan dengan kedalaman bervariasi:

from sklearn.tree import DecisionTreeRegressor
train_scores, test_scores = [], []

for depth in range(1, 10):
    model = DecisionTreeRegressor(max_depth=depth)
    model.fit(X_train, y_train)
    train_scores.append(model.score(X_train, y_train))
    test_scores.append(model.score(X_test, y_test))
2. Plot Hasil:
import matplotlib.pyplot as plt
plt.plot(range(1, 10), train_scores, label='Training Score')
plt.plot(range(1, 10), test_scores, label='Testing Score')
plt.legend()
plt.show()
Studi Kasus: Dataset Diabetes
Tujuan: Eksperimen dengan kedalaman pohon yang berbeda untuk mengamati overfitting dan underfitting.

Cara Menyelesaikan Studi Kasus

Melatih Model dengan Kedalaman Berbeda: Latih pohon keputusan dengan nilai max_depth yang berbeda-beda.
Mengevaluasi Kinerja: Ukur skor pelatihan dan pengujian untuk setiap kedalaman.
Mendiagnosis Overfitting/Underfitting: Identifikasi kedalaman di mana skor pelatihan mulai berbeda jauh dari skor pengujian.
Memilih Kedalaman Optimal: Pilih kedalaman yang menyeimbangkan bias dan variansi.
3.2 Kurva Validasi dan Kurva Pembelajaran
Kurva validasi menunjukkan bagaimana performa model berubah dengan parameter tertentu, sedangkan kurva pembelajaran menggambarkan dampak dari meningkatnya ukuran data pelatihan.

Langkah-Langkah Pembuatan Kurva Pembelajaran:

Generate kurva pembelajaran:

from sklearn.model_selection import learning_curve

train_sizes, train_scores, test_scores = learning_curve(
    LinearRegression(), X, y, cv=5, scoring='neg_mean_squared_error')
Plot hasil:

train_mean = -train_scores.mean(axis=1)
test_mean = -test_scores.mean(axis=1)
plt.plot(train_sizes, train_mean, label='Training Error')
plt.plot(train_sizes, test_mean, label='Validation Error')
plt.legend()
plt.show()
Studi Kasus: Dataset Kualitas Anggur Tujuan: Analisis apakah menambah lebih banyak sampel meningkatkan prediksi kualitas anggur.

Cara Menyelesaikan Studi Kasus

Menghasilkan Kurva Pembelajaran: Gunakan learning_curve untuk menganalisis kinerja model dengan ukuran pelatihan yang bervariasi.
Memplot Hasil: Visualisasikan kesalahan pelatihan dan validasi.
Menginterpretasi Temuan: Tentukan apakah menambahkan lebih banyak data meningkatkan kinerja atau apakah model telah mencapai plateau.
3.3 Trade-off Bias vs. Variance
Bias merujuk pada kesalahan akibat asumsi yang terlalu sederhana, sedangkan varians mengukur sensitivitas terhadap fluktuasi kecil dalam data pelatihan. Menyeimbangkan keduanya adalah kunci untuk generalisasi.

from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

# Membandingkan Linear Regression dengan Ridge Regression
linear_scores = cross_val_score(LinearRegression(), X, y, cv=5, scoring='neg_mean_squared_error')
ridge_scores = cross_val_score(Ridge(alpha=1.0), X, y, cv=5, scoring='neg_mean_squared_error')

print("Linear Regression MSE:", -linear_scores.mean())
print("Ridge Regression MSE:", -ridge_scores.mean())
Studi Kasus Dataset: Pengeluaran Iklan
Tujuan: Membandingkan model linier dan terregularisasi untuk meminimalkan bias dan varians.

Cara Menyelesaikan Studi Kasus

Latih Model Linier dan Ridge: Latih kedua model pada dataset yang sama.

Evaluasi Kinerja: Gunakan validasi silang untuk membandingkan skor MSE.

Analisis Dampak Regularisasi: Amati bagaimana regularisasi mempengaruhi besar koefisien dan kinerja model.

# 4. Penyempurnaan Hyperparameter
4.1 Penyempurnaan Manual
Hyperparameter mengontrol perilaku algoritma ML. Menyesuaikan secara manual dapat membantu memahami dampaknya.

# Contoh: Menyesuaikan max_depth untuk pohon keputusan
for depth in [3, 5, 10]:
            model = DecisionTreeRegressor(max_depth=depth)
            scores = cross_val_score(model, X, y, cv=5)
            print(f"Depth={depth}, Mean CV Score={scores.mean()}")

Studi Kasus

Dataset: Permintaan Sewa Sepeda
Tujuan: Menyempurnakan kedalaman pohon keputusan untuk mengoptimalkan prediksi permintaan sewa.

Cara Menyelesaikan Studi Kasus

1. Tentukan Rentang Hyperparameter: Uji berbagai nilai untuk max_depth.

2. Lakukan Cross-Validation: Gunakan cross_val_score untuk mengevaluasi kinerja pada setiap nilai.

3. Pilih Nilai Optimal: Pilih kedalaman dengan skor cross-validation terbaik.

4.2 Penyempurnaan Otomatis
Pencarian grid dan pencarian acak mengotomatisasi penyempurnaan hyperparameter dengan secara sistematis menjelajahi kombinasi-kombinasi yang ada.

from sklearn.model_selection import GridSearchCV

# Tentukan Grid Parameter
param_grid = {'max_depth': [3, 5, 10], 'min_samples_split': [2, 5, 10]}


            
# Lakukan Pencarian Grid (Grid Search)
grid_search = GridSearchCV(DecisionTreeRegressor(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

print("Best Parameters:", grid_search.best_params_)

            

Studi Kasus

Dataset: Kanker Payudara Wisconsin
Tujuan: Gunakan pencarian grid untuk menemukan hyperparameter optimal untuk pohon klasifikasi.

Cara Menyelesaikan Studi Kasus

Tentukan Grid Parameter: Tentukan rentang untuk max_depth, min_samples_split, dll.

Lakukan Pencarian Grid: Gunakan GridSearchCV untuk menemukan kombinasi terbaik.

Evaluasi Model Akhir: Latih model dengan parameter terbaik dan evaluasi kinerjanya.

# 5. Model Linier
5.1 Intuisi tentang Model Linier
Model linier mengasumsikan hubungan linier antara fitur dan target. Model ini mudah dipahami dan efisien secara komputasional.

# Sesuaikan Model Regresi Linier model = LinearRegression()
model.fit(X_train, y_train)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
Studi Kasus
Dataset:  Auto MPG
Tujuan: Memprediksi konsumsi bahan bakar mobil menggunakan displacement mesin dan tenaga kuda.

Cara Menyelesaikan Studi Kasus

Persiapkan Fitur: Pilih fitur yang relevan (misalnya, displacement, tenaga kuda).

Latih Model Linier: Sesuaikan model regresi linier.

Interpretasi Koefisien: Analisis koefisien untuk memahami kontribusi fitur.

Evaluasi Model: Hitung MSE dan skor R² untuk menilai kinerja model.

5.2 Regresi Linear
Regresi linier meminimalkan jumlah kuadrat residual untuk menemukan garis terbaik.

# Mengevaluasi linear regression
y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = model.score(X_test, y_test)

    print(f"MSE: {mse}, R²: {r2}")
Studi Kasus
Dataset: Insurance Charges

Cara Menyelesaikan Studi Kasus

Feature Selection: Include features like age, bmi, and smoker.

Train Model: Fit a linear regression model.

Evaluate Metrics: Compute MSE, MAE, and R² score.

Visualize Results: Plot predicted vs. actual values.

5.3 Regularisasi pada Model Linier
Regularisasi memberikan penalti pada koefisien besar untuk mencegah overfitting.

from sklearn.linear_model import Ridge

# Fit ridge regression
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
print("Ridge Coefficients:", ridge.coef_)
Studi Kasus
Dataset: Kekuatan Beton
Tujuan: memprediksi kekuatan tekan menggunakan model linier terregularisasi.

Cara Menyelesaikan Studi Kasus

Terapkan Regularisasi: Gunakan regresi Ridge atau Lasso.

Bandingkan Model: Evaluasi kinerja terhadap model tanpa regularisasi.

Sesuaikan Alpha: Sesuaikan kekuatan regularisasi untuk menyeimbangkan bias dan varians.

5.4 Model Linier untuk Klasifikasi
Regresi logistik memperluas model linier untuk tugas klasifikasi biner.

from sklearn.linear_model import LogisticRegression

# Fit logistic regression
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
print("Accuracy:", log_reg.score(X_test, y_test))
Studi Kasus
Dataset: Default Kartu Kredit,
Tujuan: memprediksi risiko gagal bayar menggunakan demografi pelanggan dan riwayat pembayaran.

Cara Menyelesaikan Studi Kasus

Persiapkan Fitur: Sertakan fitur seperti pendapatan, limit_kredit, dan riwayat_pembayaran.

Latih Model Logistik: Sesuaikan model regresi logistik.

Evaluasi Metrik: Hitung akurasi, presisi, recall, dan skor F1.

Interpretasi Koefisien: Analisis pentingnya fitur.

# 6. Model Pohon Keputusan (Decision Tree)
6.1 Intuisi tentang Model Berbasis Pohon
Pohon keputusan membagi ruang fitur secara rekursif ke dalam region-region.

from sklearn.tree import DecisionTreeClassifier, export_text

tree = DecisionTreeClassifier(max_depth=3)
tree.fit(X_train, y_train)

rules = export_text(tree, feature_names=list(X.columns))
print(rules)
Studi Kasus: Dataset Spesies Iris,
tujuan mengklasifikasikan spesies bunga menggunakan pengukuran kelopak dan sepal.

Cara Menyelesaikan Studi Kasus

Latih Pohon Keputusan: Sesuaikan klasifikasi pohon keputusan.

Visualisasikan Aturan: Gunakan export_text untuk menginterpretasikan pohon.

Evaluasi Kinerja: Hitung akurasi dan matriks kebingungannya.

6.2 Pohon Keputusan dalam Klasifikasi
Pohon klasifikasi menetapkan kelas berdasarkan mayoritas dalam node daun.

accuracy = tree.score(X_test, y_test)
print(f"Accuracy: {accuracy}")
Studi Kasus: Dataset Churn Pelanggan, memprediksi kemungkinan churn menggunakan data penggunaan layanan dan informasi penagihan.

Cara Menyelesaikan Studi Kasus

Persiapkan Fitur: Sertakan fitur seperti monthly_charges, tenure, dan contract_type.

Latih Pohon Keputusan: Sesuaikan pohon klasifikasi.

Evaluasi Metrik: Hitung akurasi, presisi, recall, dan ROC-AUC.

6.3 Pohon Keputusan dalam Regresi
Pohon regresi memprediksi hasil kontinu dengan rata-rata nilai dalam simpul daun.

from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor(max_depth=3)
tree_reg.fit(X_train, y_train)
Studi Kasus: Dataset Permintaan Sewa Sepeda, memprediksi sewa sepeda harian berdasarkan kondisi cuaca.

Persiapkan fitur: suhu, kelembapan, kondisi cuaca.
Latih model regresi.
Evaluasi MSE, MAE, dan R².
6.4 Hiperparameter dari Pohon Keputusan
Hiperparameter utama meliputi max_depth, min_samples_split, dan min_samples_leaf.

from sklearn.model_selection import GridSearchCV

param_grid = {'max_depth': [3, 5, 10]}
grid_search = GridSearchCV(DecisionTreeRegressor(), param_grid, cv=5)
grid_search.fit(X_train, y_train)
Studi Kasus: Dataset Kebisingan Sayap Pesawat

Definisikan grid parameter.
Lakukan pencarian grid.
Latih dan evaluasi model akhir.


# 7. Ensemble Model
7.1 Metode Ensemble Menggunakan Bootstrapping
Bagging menggabungkan beberapa weak learners pada sampel bootstrap.

from sklearn.ensemble import RandomForestRegressor

# Train random forest
rf = RandomForestRegressor(n_estimators=100)
rf.fit(X_train, y_train)
Studi Kasus: Dataset Tipe Penutup Hutan

Latih Random Forest.
Evaluasi akurasi atau skor F1.
Analisis feature_importances_.
7.2 Ensemble Berdasarkan Boosting
Boosting melatih model secara berurutan memperbaiki kesalahan sebelumnya.

from sklearn.ensemble import GradientBoostingRegressor

gb = GradientBoostingRegressor(n_estimators=100)
gb.fit(X_train, y_train)
Studi Kasus: Dataset Harga Airbnb

Latih model Gradient Boosting.
Evaluasi MSE atau RMSE.
Sesuaikan hyperparameter seperti n_estimators dan learning_rate.
Cara Menyelesaikan Studi Kasus

Melatih Gradient Boosting: Melatih model gradient boosting.
Mengevaluasi Metrik: Menghitung MSE atau RMSE.
Menyetel Hyperparameter: Menyesuaikan n_estimators, learning_rate, dll.
7.3 Penyetelan Hiperparameter dengan Metode Ensemble
Penyetelan hiperparameter memaksimalkan kinerja model ensemble.

param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [3, 5, 10]}
grid_search = GridSearchCV(RandomForestRegressor(), param_grid, cv=5)
grid_search.fit(X_train, y_train)
Studi Kasus: Dataset Penjualan Online

Definisikan grid parameter.
Lakukan Grid Search.
Latih model dengan parameter optimal.
Cara Menyelesaikan Studi Kasus

Mendefinisikan Parameter Grid: Menentukan rentang untuk n_estimators dan max_depth.
Melakukan Grid Search: Menggunakan GridSearchCV untuk menemukan kombinasi terbaik.
Mengevaluasi Model Akhir: Melatih dan mengevaluasi model yang dioptimalkan.


# 8. Evaluasi Kinerja Model
8.1 Membandingkan Model dengan Baseline Sederhana
Baseline memberikan titik referensi untuk membandingkan kinerja model.

from sklearn.dummy import DummyRegressor

dummy = DummyRegressor(strategy='mean')
dummy.fit(X_train, y_train)
baseline_mse = mean_squared_error(y_test, dummy.predict(X_test))
Studi Kasus: Harga Saham, tujuan membandingkan model baseline dan model ML untuk prediksi harga saham.

Cara Menyelesaikan Studi Kasus

Latih Model Baseline: Sesuaikan model dummy regressor.

Latih Model ML: Sesuaikan model yang lebih kompleks (misalnya, regresi linear).

Bandingkan Metode: Evaluasi kedua model menggunakan MSE atau MAE.

8.2 Pilihan Cross-Validation
from sklearn.model_selection import StratifiedKFold, cross_val_score

cv = StratifiedKFold(n_splits=5)
scores = cross_val_score(model, X, y, cv=cv)
Studi Kasus: Penyakit Jantung, tujuan gunakan stratified k-fold untuk distribusi kelas yang seimbang.

Cara Menyelesaikan Studi Kasus

Tentukan Stratified K-Fold: Gunakan StratifiedKFold untuk memastikan pembagian yang seimbang.

Evaluasi Model: Hitung skor cross-validation.

Interpretasi Hasil: Analisis kinerja di seluruh fold.

8.3 Nested Cross-Validation
from sklearn.model_selection import KFold

outer_cv = KFold(n_splits=5)
nested_scores = cross_val_score(grid_search, X, y, cv=outer_cv)
Studi Kasus: Pinjaman Default, tujuan implementasikan nested CV untuk estimasi kinerja yang tidak bias.

Cara Menyelesaikan Studi Kasus

Tentukan Inner dan Outer Loops: Gunakan loop bersarang untuk tuning dan evaluasi.

Lakukan Nested CV: Gunakan cross_val_score dengan GridSearchCV.

Laporkan Hasil: Ringkas kinerja di seluruh fold.

8.4 Metode Klasifikasi
Evaluasi klasifikasi menggunakan precision, recall, dan F1-score.

from sklearn.metrics import classification_report

report = classification_report(y_test, y_pred)
print(report)
Studi Kasus: Deteksi Spam, tujuan evaluasi klasifikasi email spam menggunakan precision dan recall.

Cara Menyelesaikan Studi Kasus

Latih Klasifikasi: Sesuaikan model klasifikasi.

Buat Laporan: Gunakan classification_report untuk menghitung metrik.

Interpretasi Hasil: Fokus pada precision, recall, dan F1-score.

8.5 Metrik Regresi
Evaluasi regresi menggunakan MAE, RMSE, dan R².

from sklearn.metrics import mean_absolute_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
Studi Kasus: Harga Rumah, tujuan menilai model regresi menggunakan MAE dan R².

Cara Menyelesaikan Studi Kasus

Latih Model Regresi: Sesuaikan model regresi.

Hitung Metrik: Hitung MAE, RMSE, dan R².

Interpretasi Hasil: Analisis kinerja dan identifikasi area untuk perbaikan.

