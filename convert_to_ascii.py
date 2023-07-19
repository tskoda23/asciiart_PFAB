from PIL import Image

im = Image.open("ascii-pineapple.jpg")
print("Image loaded with widht {0}px and height {1}px\n".format(im.width, im.height))


pixel_data = list(im.getdata())

print("This is pixel data for this image\n")
print(pixel_data)
