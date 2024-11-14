import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menampilkan citra
def show_images(images, titles):
    plt.figure(figsize=(15, 10))
    for i in range(len(images)):
        plt.subplot(2, 3, i + 1)
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
        plt.title(titles[i])
        plt.axis('off')
    plt.show()

# Baca citra berwarna
image_color = cv2.imread("C:\\Users\\user\\Downloads\\images.jpg")
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)

# Low-pass filter (Gaussian Blur)
low_pass_color = cv2.GaussianBlur(image_color, (15, 15), 0)
low_pass_gray = cv2.GaussianBlur(image_gray, (15, 15), 0)

# High-pass filter
# High-pass filter dapat dilakukan dengan mengurangkan low-pass dari citra asli
high_pass_color = cv2.subtract(image_color, low_pass_color)
high_pass_gray = cv2.subtract(image_gray, low_pass_gray)

# High-boost filter
# Menggabungkan citra asli dengan high-pass
boost_factor = 1.5
high_boost_color = cv2.addWeighted(image_color, boost_factor, high_pass_color, 1 - boost_factor, 0)
high_boost_gray = cv2.addWeighted(image_gray, boost_factor, high_pass_gray, 1 - boost_factor, 0)

# Tampilkan hasil
show_images(
    [image_color, low_pass_color, high_pass_color, 
     image_gray, low_pass_gray, high_pass_gray],
    ['Original Color', 'Low-Pass Color', 'High-Pass Color',
     'Original Grayscale', 'Low-Pass Grayscale', 'High-Pass Grayscale']
)

show_images(
    [image_color, high_boost_color, 
     image_gray, high_boost_gray],
    ['Original Color', 'High-Boost Color', 
     'Original Grayscale', 'High-Boost Grayscale']
)