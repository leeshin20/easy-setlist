from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import os

def create_setlist_image(track_infos, output_path="setlist_output.png"):
    item_height = 120
    width = 800
    height = item_height * len(track_infos)

    img = Image.new("RGB", (width, height), color = "white")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("Arial.ttf", size = 24)
    except:
        font = ImageFont.load_default()

    for i, track in enumerate(track_infos):
        y_offset = i * item_height

        try:
            response = requests.get(track['image_url'])
            cover = Image.open(BytesIO(response.content)).resize((100, 100))
        except:
            cover = Image.new("RGB", (100, 100), color="gray")

        img.paste(cover, (20, y_offset + 10))

        draw.text((140, y_offset + 20), f"{track['title']}", font=font, fill="black")
        draw.text((140, y_offset + 60), f"by {track['artist']}", font=font, fill="gray")

    img.save(output_path)
    print(f"이미지 저장 완료: {output_path}")