from setlist.spotify_service import search_track_info
from setlist.image_service import create_setlist_image

titles = [
    "Beyond the time",
    "get wild",
    "ディストーション",
    "Rising Hope",
    "美少女無罪♡パイレーツ",
    "原罪のレクイエム",
    "Daylight Sinfonia"
]

track_infos = []
for title in titles:
    info = search_track_info(title)
    if info:
        track_infos.append(info)
    else:
        print(f"곡 정보를 찾을 수 없습니다 : {title}")

create_setlist_image(track_infos)