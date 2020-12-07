from PIL import Image, ImageDraw, ImageEnhance
import os
import sys

if len(sys.argv) != 3:
    print('Give 2 arguments - the name of the encrypted file and type of decryption')
    exit()
infile = str(sys.argv[1])
foo = str(sys.argv[2])

if not os.path.isfile(infile):
    print('That file does not exist.')
    exit()

file, e = os.path.splitext(infile)
input_file_1 = file + '_1.bmp'
input_file_2 = file + '_2.bmp'

img = Image.open(input_file_2)
print("Image size: {}".format(img.size))

background = Image.open(input_file_1)

background.paste(img, (0, 0), img)
background.save('decrypt-' + infile, "JPEG")
background.show()
print('Done.')

