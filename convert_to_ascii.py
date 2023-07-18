from PIL import Image

im = Image.open("ascii-pineapple.jpg")
print("Image loaded with widht {0}px and height {1}px".format(im.width, im.height))
