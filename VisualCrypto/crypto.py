from PIL import Image, ImageDraw
import os
import sys
from random import SystemRandom

random = SystemRandom()
xrange = range

if len(sys.argv) != 2:
    print('Give one argument - the name of the file to be encrypted')
    exit()
infile = str(sys.argv[1])

if not os.path.isfile(infile):
    print('That file does not exist.')
    exit()

img = Image.open(infile)

file, e = os.path.splitext(infile)
out_filename_1 = file + '_1.png'
out_filename_2 = file + '_2.png'

img = img.convert('1')

print("Image size: {}".format(img.size))

width = img.size[0] * 2
height = img.size[1] * 2

#print("{} x {}".format(width, height))

output_image_1 = Image.new('1', (width, height))
output_image_2 = Image.new('1', (width, height))
draw_A = ImageDraw.Draw(output_image_1)
draw_B = ImageDraw.Draw(output_image_2)

patterns = ((1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1), (0, 1, 1, 0), (0, 1, 0, 1), (0, 0, 1, 1))

for x in xrange(0, int(width / 2)):
    for y in xrange(0, int(height / 2)):
        pixel = img.getpixel((x, y))
        pat = random.choice(patterns)

        draw_A.point((x * 2, y * 2), pat[0])
        draw_A.point((x * 2 + 1, y * 2), pat[1])
        draw_A.point((x * 2, y * 2 + 1), pat[2])
        draw_A.point((x * 2 + 1, y * 2 + 1), pat[3])
        if pixel == 0:
            draw_B.point((x * 2, y * 2), 1 - pat[0])
            draw_B.point((x * 2 + 1, y * 2), 1 - pat[1])
            draw_B.point((x * 2, y * 2 + 1), 1 - pat[2])
            draw_B.point((x * 2 + 1, y * 2 + 1), 1 - pat[3])
        else:
            draw_B.point((x * 2, y * 2), pat[0])
            draw_B.point((x * 2 + 1, y * 2), pat[1])
            draw_B.point((x * 2, y * 2 + 1), pat[2])
            draw_B.point((x * 2 + 1, y * 2 + 1), pat[3])

output_image_1.save(out_filename_1, 'PNG')
output_image_2.save(out_filename_2, 'PNG')
output_image_1.show()
output_image_2.show()
print('Done.')
