# requests 웹페이지 구성요소, 정보를 가져오기 위한 라이브러리 설치해야된다.!

import requests  # 리퀘스트 임포트!
from bs4 import BeautifulSoup  # BeautifulSoup 임포트!

# 리퀘스츠로 자원요청
# request.get() 메서드
print(requests.get("https://www.naver.com"))

r = requests.get("https://www.naver.com")

# print(r.content)  # 콘텐트를 사용하면 우리가 받은 자원을 원시값(16비트) 형태로 확인 가능
# 사람이 보기에는 어려워서 .text 사용(사람이 보기 쉬움)
# print(r.text)  # html구조로 출력.

# 이렇게 얻은 데이터를 파서를 이용하여 파싱하여 사용

# BeautifulSoup 라이브러리를 다운로드하여 파싱

# html.parser를 이용하여 r.content 정보를 파싱
bs = BeautifulSoup(r.content, "html.parser")

print(bs)
h3 = bs.select("h3")  # select 메서드는 응답받은 정보들 중에서 인자로 입력한 요소를 전부다 선택해줌
print(h3)  # 리스트형으로 반환
print(h3[0].text)
print(h3[1].text)
print(h3[2].text)
print(h3[3].text)
print(h3[4].text)
print(h3[0].name)  # 태그의 이름
print(h3[0].attrs)  # 태그의 속성과 값
h3 = bs.select_one("h3")  # select_one 메서드는 인자로 입력한 요소중 가장 첫번째를 반환.
print(h3)  # 리스트형으로 반환하지는 않음

print(h3.text)

h3 = bs.select_one("h3 > a")  # 자식요소를 선택할때는 ">" 기호 사용
print(h3)

selecter = bs.select_one("div.current_box")  # . 뒤에는 클래스 이름
print(selecter)

selecter = bs.select(".title")
print(selecter)
selecter = bs.select("#u_skip")  # 뒤에는 id값
print(selecter)

# selecter = bs.find_all("태그명", {"속성명": "값"})
selecter = bs.find_all("div", {"class": "partner_box"})
print(selecter)
selecter = bs.find("div", {"class": "partner_box"})
print(selecter)
print("--------------------")
print(selecter.text)
