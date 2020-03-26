from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import datetime
def loli_license(name):
    img = Image.open("loli.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("DINNextCYR-BoldItalic.otf", 60)
    today = datetime.datetime.today()
    time = today.strftime("%d.%m.%Y")
    draw.text((600, 425),name,(0,0,0),font=font)
    draw.text((520, 595),time,(0,0,0),font=font)
    img.save('loli2.png')
loli_license("я ебу собак")
