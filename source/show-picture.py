import PIL.Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_path", help="please provide path to image file")
args = parser.parse_args()

image = PIL.Image.open(args.file_path)

print(f"image has size of: {image.width} x {image.height}")
