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


im = Image.open("ascii-pineapple.jpg")
print("Image loaded with width {0}px and height {1}px\n".format(im.width, im.height))


px_data = list(im.getdata())
px_brightness_list = []
for px_tuple in px_data:
    px_brightness_list.append(avg_brightness(px_tuple))

ascii_list = ""
for px_b in px_brightness_list:
    ascii_list = ascii_list + map_brightness_to_ascii(px_b)

print(ascii_list)
