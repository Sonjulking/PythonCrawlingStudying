# 웹페이지에 들어가지 않고 뉴스 검색, 기사제목, 본문, 링크, 게시날짜를 엑셀에 담아 저장
# 뉴스 검색, 기사제목, 링크를 리스트에 담아서 출력

import requests
from bs4 import BeautifulSoup
import pandas as pd

keyword = input("검색하고자하는 키워드를 입력해주세요. > ")
r = requests.get(
    "https://news.google.com/search?q=" + keyword + "&hl=ko&gl=KR&ceid=KR%3Ako")
bs = BeautifulSoup(r.text, "html.parser")

# 기사제목, 링크

# titles = bs.select("h3 > a")
titles = bs.find_all("div", {"class": "xrnccd"})

news = []

for i in titles:
    title = i.find("h3").text
    links = links = "https://news.google.com" + i.find("a")["href"][1:]
    # description = i.find("span", {"class": "xBbh9"}).text  # 본문요약
    date = i.find("time").text

    news.append([title, links, date])
    google_news_df = pd.DataFrame(news, columns=["기사제목", "링크주소", "게시날짜"])

google_news_df.to_excel("뉴스 크롤링 결과_PRO.xlsx")
print("저장성공!")
# for i in titles:
#     title = i.text
#     links = "https://news.google.com" + i.get("href")[1:]  # get메서드 사용

#     news.append([title, links])
#     google_news_df = pd.DataFrame(news, columns=["기사제목", "링크주소"])

# google_news_df.to_excel("뉴스 크롤링 결과.xlsx")
# print("저장성공")

# print(google_news_df)
