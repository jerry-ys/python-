import qrcode
from PIL import Image,ImageDraw

def generate_qrcode(url,output,version=1,correct=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,logo=None,logo_size=None,padding=5):
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
        img_w,img_h = img.size
        draw = ImageDraw.Draw(img)
        circle_x = img_w / 2
        circle_y = img_h / 2
        radius = logo_size[0] / 2 + padding
        draw.ellipse([circle_x - radius,
                      circle_y - radius,
                      circle_x + radius,
                      circle_y + radius],
                      fill = "yellow")

        logo = Image.open(logo).convert("RGBA")
        logo.thumbnail(logo_size)
        logo_w,logo_h = logo.size
        offset = ((img_w-logo_w) // 2,(img_h-logo_h) // 2)
        img.paste(logo,offset,logo)

    img.save(output)
    img.show()


if __name__ =="__main__":
    url = "http://fishc.com.cn"
    output = "二维码.png"
    logo = "logo.png"
    logo_size = (60,60)
    generate_qrcode(url,output,logo=logo,logo_size=logo_size,padding=10)
