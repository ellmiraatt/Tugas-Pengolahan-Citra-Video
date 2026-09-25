import cv2

# ==========================================
# MEMBACA GAMBAR
# ==========================================

image = cv2.imread('test.jpeg')

if image is None:
    print("Gambar tidak ditemukan!")
    exit()

# ==========================================
# KONVERSI RGB/BGR KE GRAYSCALE SECARA MANUAL
# ==========================================

height = image.shape[0]
width = image.shape[1]

gray = image.copy()

for i in range(height):
    for j in range(width):
        B = int(image[i, j, 0])
        G = int(image[i, j, 1])
        R = int(image[i, j, 2])

        # Rumus grayscale
        gray_value = int(0.114 * B + 0.587 * G + 0.299 * R)

        gray[i, j] = [gray_value, gray_value, gray_value]


# ==========================================
# 1. TRANSFORMASI INTENSITAS
# NEGATIVE IMAGE
# ==========================================

negative = gray.copy()

for i in range(height):
    for j in range(width):
        intensity = int(gray[i, j, 0])

        # Rumus negatif
        new_intensity = 255 - intensity

        negative[i, j] = [
            new_intensity,
            new_intensity,
            new_intensity
        ]


# ==========================================
# 2. HISTOGRAM MANUAL
# ==========================================

histogram = [0] * 256

for i in range(height):
    for j in range(width):
        intensity = int(gray[i, j, 0])
        histogram[intensity] += 1


# ==========================================
# 3. CUMULATIVE HISTOGRAM / CDF
# ==========================================

cdf = [0] * 256

cdf[0] = histogram[0]

for k in range(1, 256):
    cdf[k] = cdf[k - 1] + histogram[k]


# ==========================================
# 4. CARI CDF MINIMUM
# ==========================================

cdf_min = 0

for k in range(256):
    if cdf[k] != 0:
        cdf_min = cdf[k]
        break


# ==========================================
# 5. EKUALISASI HISTOGRAM SECARA MANUAL
# ==========================================

total_pixel = height * width

equalized = gray.copy()

for i in range(height):
    for j in range(width):

        intensity = int(gray[i, j, 0])

        # Rumus histogram equalization
        new_intensity = int(
            ((cdf[intensity] - cdf_min) /
             (total_pixel - cdf_min)) * 255
        )

        # Membatasi nilai 0 - 255
        if new_intensity < 0:
            new_intensity = 0

        if new_intensity > 255:
            new_intensity = 255

        equalized[i, j] = [
            new_intensity,
            new_intensity,
            new_intensity
        ]


# ==========================================
# MENAMPILKAN HASIL
# ==========================================

cv2.imshow('Original Image', image)
cv2.imshow('Grayscale', gray)
cv2.imshow('Intensity Transformation - Negative', negative)
cv2.imshow('Histogram Equalization', equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()