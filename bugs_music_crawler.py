import requests
from bs4 import BeautifulSoup

r = requests.get("https://music.bugs.co.kr/chart")
bs = BeautifulSoup(r.text, "html.parser")

# 노래와 가수의 목록

song_name = []
artist_name = []

song = bs.select("p.title > a")
artist = bs.select("td.left > p.artist")
# artist_set = list(set(artist))


for s in range(len(song)):
    song_name.append(song[s].text)
for a in range(len(artist)):
    artist_name.append(artist[a].text)

for i in range(0, 50):
    print(
        f"순위{i + 1}위 - 가수 : {artist_name[i].strip()}")
    print(f"곡명: {song_name[i].strip()}")
    print()
