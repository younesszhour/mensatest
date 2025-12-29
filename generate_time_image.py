
import requests
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
def generate_image_with_text(text):
    img = Image.new('L', (800, 480), color='white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((100, 200), text, fill='black')
    img.save("time.png")
def get_time():
    try:
        r = requests.get("http://worldtimeapi.org/api/timezone/Europe/Berlin")
        datetime_str = r.json()['datetime'].replace('Z', '+00:00')
        dt = datetime.fromisoformat(datetime_str)
        return dt.strftime("%d.%m.%Y %H:%M")
    except Exception as e:
        print(f"API error: {e}")
        return str(datetime.now())
if __name__ == "__main__":
    generate_image_with_text(get_time())
