from PIL import Image

_ASCII_ARR = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

razmak = 256 / len(_ASCII_ARR)
_ASCII_MAP = {}

j = 1

for i in range(0, 256):
    if i > razmak * j:
        j = j + 1
    _ASCII_MAP[i] = j


def avg_brightness(px_tuple):
    return int((px_tuple[0] + px_tuple[1] + px_tuple[2]) / 3)


def map_brightness_to_ascii(brightness):
    return _ASCII_ARR[_ASCII_MAP[brightness]]


big_im = Image.open("ascii-pineapple.jpg")

small_w = round(big_im.width / 10)
small_h = round(big_im.height / 10)
print(small_w)
print(small_h)
im = big_im.resize((small_w, small_h))
print("Image loaded with width {0}px and height {1}px\n".format(im.width, im.height))


all_px_data = list(im.getdata())

px_matrix = []
x = 0


for i in range(0, len(all_px_data)):
    for j in range(0, im.width):
        line = map_brightness_to_ascii(avg_brightness(all_px_data[i]))
        i = i + 1
        print(line, end=" ")
    print("\n")
    px_matrix.append(line)
