import cv2

# MEMBACA GAMBAR

image = cv2.imread('test.jpeg')

if image is None:
    print("Gambar tidak ditemukan!")
    exit()


# ==========================================
# KONVERSI KE GRAYSCALE SECARA MANUAL
# ==========================================

height = image.shape[0]
width = image.shape[1]

gray = image.copy()

for i in range(height):
    for j in range(width):

        B = int(image[i, j, 0])
        G = int(image[i, j, 1])
        R = int(image[i, j, 2])

        gray_value = int(
            0.114 * B +
            0.587 * G +
            0.299 * R
        )

        gray[i, j] = [
            gray_value,
            gray_value,
            gray_value
        ]


# ==========================================
# FILTER SPASIAL - BLUR / AVERAGING
# ==========================================

blur = gray.copy()

for i in range(1, height - 1):
    for j in range(1, width - 1):

        total = 0

        # Kernel 3x3
        for x in range(-1, 2):
            for y in range(-1, 2):

                total += int(
                    gray[i + x, j + y, 0]
                )

        # Rata-rata 9 pixel
        value = int(total / 9)

        blur[i, j] = [
            value,
            value,
            value
        ]


# ==========================================
# FILTER SPASIAL - SHARPENING
# ==========================================

sharpen = gray.copy()

# Kernel sharpening
kernel = [
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
]

for i in range(1, height - 1):
    for j in range(1, width - 1):

        total = 0

        for x in range(-1, 2):
            for y in range(-1, 2):

                pixel = int(
                    gray[i + x, j + y, 0]
                )

                kernel_value = kernel[x + 1][y + 1]

                total += pixel * kernel_value

        # Membatasi nilai 0-255
        if total < 0:
            total = 0

        if total > 255:
            total = 255

        sharpen[i, j] = [
            total,
            total,
            total
        ]


# ==========================================
# MENAMPILKAN HASIL
# ==========================================

cv2.imshow('Original Image', image)
cv2.imshow('Grayscale', gray)
cv2.imshow('Spatial Filter - Blur', blur)
cv2.imshow('Spatial Filter - Sharpen', sharpen)

cv2.waitKey(0)
cv2.destroyAllWindows()
