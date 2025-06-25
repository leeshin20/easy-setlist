# app.py

from setlist.spotify_service import search_track_info
from setlist.image_service import create_setlist_image

# 🎵 입력 데이터: [제목, 아티스트]
songs = [
    ["原罪のレクイエム", "Kotoko"],
    ["Rising Hope", "LiSA"],
    ["LOVE & JOY", "城ヶ崎莉嘉 (山本希望)"],
    ["Re-sublimity", "KOTOKO"]
]

# 🎯 Spotify 검색 + 결과 수집
track_infos = []
for title, artist in songs:
    info = search_track_info(title, artist)
    if info:
        track_infos.append(info)
    else:
        print(f"❌ 검색 실패: {title} by {artist}")

# 🖼 이미지 생성
create_setlist_image(track_infos)
