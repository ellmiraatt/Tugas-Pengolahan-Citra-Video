import cv2

image = cv2.imread('test.jpeg')

if image is None:
    print("Gambar tidak ditemukan!")
else:
    print("Gambar berhasil dibaca.")


import cv2

image = cv2.imread('test.jpeg')

if image is None:
    print("Gambar tidak ditemukan!")
else:
    print("Gambar berhasil dibaca.")

    cv2.imshow('Original Image', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
import cv2
import numpy as np

# Membaca gambar
image = cv2.imread('test.jpeg')

if image is None:
    print("Gambar tidak ditemukan!")

else:
    # Membuat layer warna merah
    red_layer = np.zeros_like(image)
    red_layer[:, :] = (0, 0, 255)

    # Menggabungkan foto dengan warna merah
    result = cv2.addWeighted(image, 0.5, red_layer, 0.5, 0)

    # Menampilkan
    cv2.imshow('Original Image', image)
    cv2.imshow('Red Filter', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()