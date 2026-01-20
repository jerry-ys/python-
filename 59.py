from PIL import Image

img = Image.open("fishc.jpg")
out = img.convert("L")
width,height = out.size
out = out.resize((int(width),int(height*0.35)))
width,height = out.size
asciis = "@%#*+=-:. "
text = ""
for row in range(height):
    for col in range(width):
        gray = out.getpixel((col,row))
        text += asciis[int(gray / 255 * 9)]
    text += "\n"

with open("mm.txt","w") as f:
    f.write(text)