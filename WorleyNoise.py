import math
import random
from PIL import Image, ImageDraw

imgx = 800  # rozdzielczość
imgy = 800

image = Image.new("RGB", (imgx, imgy))
draw = ImageDraw.Draw(image)
pixels = image.load()
n = 500  #  liczba punktów ziarnistych
m = 1 # stopień złożoności wzoru (czyli stopień "ziarnistości"

seedsX = [random.randint(0, imgx - 1) for i in range(n)]
seedsY = [random.randint(0, imgy - 1) for i in range(n)]

# maksymalny dystans
maxDist = 0.0
for ky in range(imgy):
    for kx in range(imgx):
        dists = [math.hypot(seedsX[i] - kx, seedsY[i] - ky) for i in range(n)]
        dists.sort()
        if dists[m] > maxDist:
            maxDist = dists[m]

#  gradient kolorów w tle (niebieski do fioletowego)
for ky in range(imgy):
    for kx in range(imgx):
        gradient_color = (0, 0, int(255 * ky / imgy))  # Gradient kolorów od niebieskiego do fioletowego
        pixels[kx, ky] = gradient_color

#  punkty ziarniste
for ky in range(imgy):
    for kx in range(imgx):
        dists = [math.hypot(seedsX[i] - kx, seedsY[i] - ky) for i in range(n)]
        dists.sort()
        c = int(round(255 * dists[m] / maxDist))
        pixels[kx, ky] = (0, 0, c)

image.save("WorleyNoise.png", "PNG")