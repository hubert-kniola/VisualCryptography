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
input_file_1 = file + '_1.png'
input_file_2 = file + '_2.png'

img = Image.open(input_file_1)
print("Image size: {}".format(img.size))

if foo == 'B':
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(0.8)
elif foo == 'L':
    img = img.convert('L')
elif foo == 'C':
    enh = ImageEnhance.Contrast(img)
    enh.enhance(1.3).show("30% more contrast")
else:
    print('Give 2 arguments')

background = Image.open(input_file_2)

background.paste(img, (0, 0), img)
background.save('decrypt-' + infile, "PNG")
background.show()
print('Done.')

