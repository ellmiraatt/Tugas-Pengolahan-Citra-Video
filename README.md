
Repositori ini berisi implementasi praktis pemrosesan citra digital dan pengolahan video menggunakan Python. Terdapat tiga skrip utama dengan cakupan materi berikut:

# 1. `1-Intro.py` — Pengenalan Pemrosesan Citra & Video
* Membaca Citra (Read Image): Mengimpor citra dari direktori lokal ke dalam matriks data.
* Menampilkan Citra (Show Image): Menampilkan citra menggunakan jendela tampilan grafik (display window).
* Filter Warna Citra (Color Filtering - Image): Ekstraksi dan manipulasi ruang warna (seperti RGB, HSV, atau Gray) pada citra diam.
* Filter Warna Video (Color Filtering - Video): Penerapan filter warna secara real-time pada alur frame video/webcam.

# 2. `2-ti-eq.py` — Transformasi Intensitas & Ekualisasi Histogram
* Transformasi Intensitas (Intensity Transformation): Manipulasi nilai piksel (seperti operasi negative, log transformation, atau gamma correction).
* Ekualisasi Histogram (Histogram Equalization): Meredistribusikan tingkat keabuan citra untuk meningkatkan kontras.
* Catatan Khusus: Implementasi seluruh algoritma dibangun secara manual murni dari dasar (from scratch) dengan memanfaatkan kalkulasi matriks, tanpa menggunakan fungsi bawaan (built-in functions) dari perpustakaan OpenCV (`cv2.equalizeHist`) maupun package pendukung lainnya.

# 3. `3-filter-spasial.py` — Pengolahan Filter Spasial
* Penerapan Filter Spasial (Spatial Filtering): Proses konvolusi 2D pada citra menggunakan matriks kernel/mask.
* Cakupan Pemrosesan:
* Smoothing Filter: Mengurangi noise atau mengaburkan citra (contoh: Average/Mean Filter, Gaussian Filter).
* Sharpening Filter: Memperjelas tepi dan detail citra (contoh: Laplacian Filter, High-pass Filter).
