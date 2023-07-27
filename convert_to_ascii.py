#!/usr/bin/env python3
from PIL import Image
import numpy
import sys

# GLOBALS

_ASCII_ARR = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
_ASCII_ARR_INV = _ASCII_ARR[::-1]
_ASCII_MAP = {}
_OKGREEN = "\033[92m"


def init():
    global _ASCII_ARR
    global _ASCII_MAP

    space = 256 / (len(_ASCII_ARR) - 1)

    j = 1

    for i in range(0, 256):
        if i > space * j:
            j = j + 1
        _ASCII_MAP[i] = j


def min_max_b(px_tuple):
    return int(
        (
            max(px_tuple[0], px_tuple[1], px_tuple[2])
            + min(px_tuple[0], px_tuple[1], px_tuple[2])
        )
        / 2
    )


def lum_b(px_tuple):
    return int(
        numpy.sqrt(
            0.299 * numpy.square(px_tuple[0])
            + 0.587 * numpy.square(px_tuple[1])
            + 0.114 * numpy.square(px_tuple[2])
        )
    )


def avg_b(px_tuple):
    return int((px_tuple[0] + px_tuple[1] + px_tuple[2]) / 3)


def get_brightness(px_tuple, b_type):
    if b_type == 0:
        return avg_b(px_tuple)
    elif b_type == 1:
        return min_max_b(px_tuple)
    elif b_type == 2:
        return lum_b(px_tuple)
    else:
        return avg_b(px_tuple)


def map_brightness_to_ascii(brightness, invert):
    global _ASCII_MAP

    if invert == 1:
        global _ASCII_ARR_INV
        return _ASCII_ARR_INV[_ASCII_MAP[brightness]]
    else:
        global _ASCII_ARR
        return _ASCII_ARR[_ASCII_MAP[brightness]]


def convert_to_ascii(scale=10, b_type=0, invert=0, image="ascii-pineapple.jpg"):
    big_im = Image.open(image)

    small_w = round(big_im.width / scale)
    small_h = round(big_im.height / scale)
    im = big_im.resize((small_w, small_h))

    all_px_data = im.getdata()
    b_data = []
    for px in all_px_data:
        b_data.append(get_brightness(px, b_type))

    px_matrix = numpy.reshape(b_data, (im.height, im.width))

    painting = ""
    for row in px_matrix:
        line = ""
        for col in row:
            ascii = map_brightness_to_ascii(col, invert)
            line = line + ascii + ascii + ascii
        painting = painting + line + "\n"

    return painting


if __name__ == "__main__":
    init()
    ascii_art = ""
    if len(sys.argv) > 4:
        print(sys.argv[4])
        ascii_art = convert_to_ascii(
            int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
        )
    elif len(sys.argv) > 3:
        ascii_art = convert_to_ascii(
            int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
        )
    elif len(sys.argv) > 2:
        ascii_art = convert_to_ascii(int(sys.argv[1]), int(sys.argv[2]))
    elif len(sys.argv) > 1:
        ascii_art = convert_to_ascii(int(sys.argv[1]))
    else:
        ascii_art = convert_to_ascii()

    print(_OKGREEN + ascii_art)
