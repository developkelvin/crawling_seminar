# Created by kelvin at 2018-09-26
import requests
from bs4 import BeautifulSoup

# url 지정
url = "http://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3646&id=kr_010802000000"
# 요청을 하고 서버로 부터의 응답을 받아옴
response = requests.get(url)

# Status Code 출력
print("status code : ", response.status_code)

# 요청결과에서 텍스트(=html)만 가져옴
dongguk_html = response.text

# beautifulSoup에서 가져온 html 텍스트를 자체적으로 분석(파싱)하여 쉽게 특정 태그를 가져올 수 있도록 함
soup = BeautifulSoup(dongguk_html, "html.parser")

# 잘 가져왔는지 테스트. 정상적으로 가져왔으면 <title>일반공지 [1]</title>라는 글자가 출력됨

print(soup.title)

notice_table_selector = '#board_list'

notice_table = soup.select_one(notice_table_selector)

notice_list_tr = notice_table.find_all('tr')

for article in notice_list_tr:
    title = article.select_one('td.title')
    if title:
        print('제목 : ', title.get_text())


