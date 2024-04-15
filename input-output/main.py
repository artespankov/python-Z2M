from PIL import Image, ImageFilter


img = Image.open('./images/208_astro.jpg')
print(img.size)
img.thumbnail((400, 400))
img.save("astro_thumb.jpg", "jpeg")

#
# if __name__ == "__main__":
