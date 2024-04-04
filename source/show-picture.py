import PIL.Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_path", help="please provide path to image file")
args = parser.parse_args()

image = PIL.Image.open(args.file_path)

print(f"image has size of: {image.width} x {image.height}")

pixels = image.load()
for y in range(image.height):
    for x in range(image.width):
        (r, g, b) = pixels[x, y]
        pixels[x, y] = (r, 0, 0)

image.show()
