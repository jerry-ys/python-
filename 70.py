import qrcode
from PIL import Image,ImageDraw,ImageFont
from pathlib import Path

def generate_qrcode(url,output,version=1,correct=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,logo=None,logo_size=None,custom_text=None):
    qr = qrcode.QRCode(
        version = version,
        error_correction = correct,
        box_size = box_size,
        border = border,
        )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black",back_color="white").convert("RGB")

    if logo != None and logo_size != None:
        logo = Image.open(logo).convert("RGBA")
        logo.thumbnail(logo_size)
        img_w,img_h = img.size
        logo_w,logo_h = logo.size
        offset = ((img_w-logo_w) // 2,(img_h-logo_h) // 2)
        img.paste(logo,offset,logo)

    if custom_text is not None:
        font = ImageFont.truetype("msyh.ttc",24)
        bbox = font.getbbox(custom_text)
        text_w,text_h = bbox[2] - bbox[0],bbox[3] - bbox[1]
        text_pos = ((img_w - text_w) // 2,img_h + 5)
        img_combined = Image.new('RGB',(img_w,img_h + text_h + 20))
        img_combined.paste(img,(0,0))
        draw = ImageDraw.Draw(img_combined)
        draw.text(text_pos,custom_text,font = font)
        img = img_combined

    img.save(output)

def get_url(urls_file,output_folder,logo=None,logo_size=None,custom_text=None):
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True,exist_ok=True)
    with open(urls_file,"r") as f:
        urls = f.readlines()

    for i,url in enumerate(urls,start = 1):
        url = url.strip()
        output = output_folder / f"qrcode_{i}.png"
        generate_qrcode(url,output,logo=logo,logo_size=logo_size,custom_text=custom_text)

if __name__ =="__main__":
    logo = "logo.png"
    logo_size = (60,60)
    custom_text = "一个让你发现快乐的地方"
    urls_file = "url.txt"
    output_folder = "qrcodes"
    get_url(urls_file,output_folder,logo=logo,logo_size=logo_size,custom_text=custom_text)
