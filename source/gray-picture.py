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
        brightness = (r * 30 + g * 60 + b * 10) // 100
        pixels[x, y] = (brightness, brightness, brightness)

image.show()