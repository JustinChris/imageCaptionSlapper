from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

fnt = ImageFont.truetype("arial.ttf", 30)
editedImageName = "edit.png"
imagePath = "sample.png"
text = "me looking for fish"

def editImage (imagePath, text):
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

    img.save(editedImageName)

editImage(imagePath, text)
