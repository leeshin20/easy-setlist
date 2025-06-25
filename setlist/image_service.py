# image_service.py

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import requests
import os

DEFAULT_IMAGE_PATH = "assets/default_cover.png"
FONT_PATH = "fonts/NotoSansCJK.ttc"

def create_setlist_image(track_infos, output_path="setlist_output.png"):
    item_height = 120
    width = 800
    height = item_height * len(track_infos)
    img = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype(FONT_PATH, 24, index=0)
    except Exception as e:
        print("폰트 로드 실패:", e)
        font = ImageFont.load_default()

    for i, track in enumerate(track_infos):
        y = i * item_height

        try:
            if track['앨범 커버']:
                response = requests.get(track['앨범 커버'], timeout=5)
                cover = Image.open(BytesIO(response.content)).convert("RGB").resize((100, 100))
            else:
                raise ValueError("No image")
        except:
            cover = Image.open(DEFAULT_IMAGE_PATH).convert("RGB").resize((100, 100))

        img.paste(cover, (20, y + 10))

        title = track['입력 제목']
        artist = track['입력 아티스트']
        draw.text((140, y + 20), title, font=font, fill="black")
        draw.text((140, y + 60), f"by {artist}", font=font, fill="gray")

    img.save(output_path)
    print(f"✅ 세트리스트 이미지 저장 완료: {output_path}")
