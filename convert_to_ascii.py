from PIL import Image
import numpy

_ASCII_ARR = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

razmak = 256 / len(_ASCII_ARR)
_ASCII_MAP = {}

j = 1

for i in range(0, 256):
    if i > razmak * j:
        j = j + 1
    _ASCII_MAP[i] = j


def avg_brightness(px_tuple):
    brightness = int((px_tuple[0] + px_tuple[1] + px_tuple[2]) / 3)
    return brightness


def map_brightness_to_ascii(brightness):
    return _ASCII_ARR[_ASCII_MAP[brightness]]


big_im = Image.open("ascii-pineapple.jpg")

small_w = round(big_im.width / 3)
small_h = round(big_im.height / 3)
im = big_im.resize((small_w, small_h))

# print("Image loaded with width {0}px and height {1}px\n".format(im.width, im.height))

all_px_data = im.getdata()
b_data = []
for px in all_px_data:
    b_data.append(avg_brightness(px))

px_matrix = numpy.reshape(b_data, (im.height, im.width))

for row in px_matrix:
    line = ""
    for col in row:
        ascii = map_brightness_to_ascii(col)
        line = line + ascii + ascii + ascii
    print(line)
