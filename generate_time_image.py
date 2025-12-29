
import requests
from PIL import Image, ImageDraw, ImageFont
import datetime
def generate_image_with_text(text):
    img = Image.new('L', (800, 480), color='white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((100, 200), text, fill='black')
    img.save("time.png")
def get_time():
    try:
        r = requests.get("http://worldtimeapi.org/api/timezone/Europe/Berlin")
        return r.json()['datetime']
    except:
        return str(datetime.datetime.now())
if __name__ == "__main__":
    generate_image_with_text(get_time())
