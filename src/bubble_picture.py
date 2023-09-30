from PIL import Image, ImageDraw
import random

def generate_buble():

    width = 1920
    height = 1080

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    num_balls = random.randint(40,150)
    min_radius = random.randint(10,30)
    max_radius = random.randint(100,200)

    for i in range(num_balls):
        x = random.randint(min_radius, width - min_radius)
        y = random.randint(min_radius, height - min_radius)
        radius = random.randint(min_radius, max_radius)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
        draw.ellipse([(x - radius, y - radius), (x + radius, y + radius)], fill=color, outline=color)


    image.save("buble_picture.jpg",dpi=(800,800))
