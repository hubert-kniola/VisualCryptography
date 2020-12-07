from PIL import Image, ImageDraw
import os
import sys
from random import choice
import numpy as np

if len(sys.argv) != 2:
    print('Give one argument - the name of the file to be encrypted')
    exit()
infile = str(sys.argv[1])
file, e = os.path.splitext(infile)


def is_black(pixel: int) -> bool:
    return pixel < 255 // 2


def load_image(infile):
    if not os.path.isfile(infile):
        print('That file does not exist.')
        exit()
    return Image.open(infile)


def load_bitmap(infile):
    input_file_1 = file + '_1.bmp'
    input_file_2 = file + '_2.bmp'
    return Image.open(input_file_1), Image.open(input_file_2)


def gen_pixels(img):
    return np.array(img)


def encryption(img) -> (Image, Image):
    width = img.size[0]
    height = img.size[1]
    print('Original image size: {}'.format(img.size))

    pixels = gen_pixels(img)
    white_pixels: [(int, int)] = [(255, 0), (0, 255)]
    black_pixels: [((int, int), (int, int))] = [((255, 0), (0, 255)), ((0, 255), (255, 0))]

    array1, array2 = np.ndarray((height, width * 2)), np.ndarray((height, width * 2))
    print('Encrypting...')

    z = 0
    for x in range(height):
        for y in range(width):
            if is_black(pixels[x, y]):
                black1, black2 = choice(black_pixels)

                array1[x, z] = black1[0]
                array1[x, z + 1] = black1[1]
                array2[x, z] = black2[0]
                array2[x, z + 1] = black2[1]

            else:
                white1, white2 = choice(white_pixels)

                array1[x, z] = white1
                array1[x, z + 1] = white2
                array2[x, z] = white1
                array2[x, z + 1] = white2
            z += 2
        z = 0

    sh1 = Image.fromarray(array1)
    sh2 = Image.fromarray(array2)
    print('Mode: ' + sh1.mode)
    print('Generated image size: {}'.format(sh1.size))

    sh1 = sh1.convert(mode='P', colors=256)
    sh2 = sh2.convert(mode='P', colors=256)
    sh1.save(file + '_1.bmp')
    sh2.save(file + '_2.bmp')
    print('Mode: ' + sh1.mode)
    print('Generated image size: {}'.format(sh1.size))


def decryption(image1, image2) -> Image:
    image1 = Image.open(image1)
    image2 = Image.open(image2)

    width, height = image1.size
    merged = np.ndarray((height, width))
    share1, share2 = np.array(image1), np.array(image2)
    print('Decrypting...')

    for x in range(height):
        for y in range(width):
            if share1[x, y] == 255 and share2[x, y] == 255:
                merged[x, y] = 255
            else:
                merged[x, y] = 0

    mrg = Image.fromarray(merged)
    print('Mode: ' + mrg.mode)
    print('Decrypted image size: {}'.format(image1.size))

    mrg = mrg.convert(mode='P', colors=256)
    mrg.save('decrypt-' + file + '.bmp')
    print('Mode: ' + mrg.mode)
    print('Decrypted image size: {}'.format(image1.size))


if __name__ == '__main__':
    img = load_image(infile)
    encryption(img)
    decryption(file + '_1.bmp', file + '_2.bmp')
