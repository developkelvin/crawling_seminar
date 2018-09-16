# Created by kelvin at 2018-09-13
import requests
from bs4 import BeautifulSoup

# 네이버로부터 html 텍스트를 가져옴

# 가져올 url
url = "https://www.naver.com"
# 요청을 하고 서버로 부터의 응답을 받아옴
response = requests.get(url)

#Status Code 출력
print("status code : ", response.status_code)

# 요청결과에서 텍스트(=html)만 가져옴
naver_html = response.text

# beautifulSoup에서 가져온 html 텍스트를 자체적으로 분석(파싱)하여 쉽게 특정 태그를 가져올 수 있도록 함
soup = BeautifulSoup(naver_html, "html.parser")

# 잘 가져왔는지 테스트. 정상적으로 가져왔으면 NAVER라는 글자가 출력됨
print(soup.title)

# 실시간 검색어 부분 가져오기
rank_list = soup.select_one('ul.ah_l')

# 키워드 부분만 추출
rank_detail_list = soup.find_all('span', attrs={'class': 'ah_k'})

# 실시간 검색어 출력
for i in rank_detail_list:
    print(i.get_text())
