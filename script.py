from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import argparse
import os
from datetime import datetime

fnt = ImageFont.truetype("arial.ttf", 30)

def arg_parser():
    parser = argparse.ArgumentParser(
        prog="Image Caption Slapper",
        description="Image Caption Slapper is a python script used to put caption on a image with viral funny video style",
    )
    parser.add_argument("--path", "-p", help="image path", required=True)
    parser.add_argument("--text", "-t", help="text to put in the image", required=True)
    parser.add_argument("--out", "-o", help="output file name")
    return parser.parse_args()

def editImage (imagePath, text, outputName):
    editImage = Image.open(imagePath)
    editImage = editImage.convert('RGBA')
    drawer = ImageDraw.Draw(editImage)

    imagesize = editImage.size
    textSize = drawer.textbbox((0,0), text, font=fnt)
    
    targetSize = [(imagesize[0] - textSize[2]) * 0.5, imagesize[1] * 0.75]
    rectSize = [(0, imagesize[1] * 0.75), (imagesize[0], imagesize[1] * 0.84)]
    
    overlay = Image.new('RGBA', imagesize, (0,0,0) + (0,))
    drawOverlay = ImageDraw.Draw(overlay)
    drawOverlay.rectangle(xy=rectSize, fill=(0,0,0, 128))

    img = Image.alpha_composite(editImage, overlay)
    img = img.convert('RGB')

    imgDrawer = ImageDraw.Draw(img)

    imgDrawer.text(targetSize, text, font=fnt, fill=(255, 255, 255, 255), align="center")
    if not outputName:
        filename, ext = outputFileName(imagePath)
        output = filename + getcurrentdate() + "." + ext
        img.save(output)
    else:
        img.save(outputName)

def outputFileName(path):
    head, tail = os.path.split(path)
    name = tail.split(".")[0]
    ext = tail.split(".")[1]
    return name, ext

def getcurrentdate():
    now = datetime.now()
    date = str(now.year) + str(now.month) + str(now.day) + "-" + str(now.hour) + str(now.minute) + str(now.second) + str(now.microsecond)
    return date

def main():
    args = arg_parser()

    editImage(args.path, args.text, args.out)

main()