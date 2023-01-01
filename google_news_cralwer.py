# 뉴스 검색, 기사제목, 링크를 리스트에 담아서 출력

import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get(
    "https://news.google.com/search?q=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&hl=ko&gl=KR&ceid=KR%3Ako")
bs = BeautifulSoup(r.text, "html.parser")

# 기사제목, 링크

titles = bs.select("h3 > a")

news = []

for i in titles:
    title = i.text
    links = "https://news.google.com" + i.get("href")[1:]  # get메서드 사용

    news.append([title, links])
    google_news_df = pd.DataFrame(news, columns=["기사제목", "링크주소"])

google_news_df.to_excel("뉴스 크롤링 결과.xlsx")
print("저장성공")
