from PIL import Image
from pathlib import Path

images = list((Path(".") / "qrcodes").glob("*.png"))
imgs = [Image.open(img) for img in images]
img,*imgs = imgs
img.save(fp="output.gif",format="GIF",append_images=imgs,
         save_all=True,duration=200,loop=0)