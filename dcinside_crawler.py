# Created by kelvin at 2018-09-16
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests


# 식물 갤러리의 게시글을 가져온다.
def get_article(article_no):
    # 게시글을 가져올 url
    article_url = 'http://gall.dcinside.com/board/view/'
    # 쿠키를 계속 유지하기 위해 사용
    session = requests.Session()
    session.get('http://gall.dcinside.com/board/view/')
    # 사람처럼 보이게 하기 위해 다음과 같은 헤더 적용
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    gall_name = 'tree'

    params = {'id': gall_name, 'no': article_no}

    response = session.get(article_url, headers=headers, params=params)

    soup = BeautifulSoup(response.text, 'html.parser')

    article_title = soup.find('span', attrs={'class':'title_subject'}).get_text().strip()

    nickname = soup.find('span', attrs={'class':'nickname'}).get_text().strip()

    ip_address = soup.find('span', attrs={'class':'ip'}).get_text().strip()

    view_cnt = soup.find('span', attrs={'class':'gall_count'}).get_text().strip()

    comment_cnt = soup.find('span', attrs={'class':'gall_comment'}).get_text().strip()

    content_all = soup.find('div', attrs={'class': 'writing_view_box'})
    content = content_all.p.get_text().strip()

    reg_dtime = soup.find('span', attrs={'class':'gall_date'}).get_text().strip()

    article_data = (gall_name, article_no, article_title, nickname,
                    ip_address, view_cnt, comment_cnt, content, reg_dtime)

    print(article_data)

    f = open('dc_crawling_result.csv', 'a', encoding='utf8')
    for i in article_data:
        f.write(str(i)+", ")
    f.close()

if __name__ == "__main__":
    # http://gall.dcinside.com/board/view/?id=tree&no=243965 이 URL의 게시글을 크롤링 함.
    get_article(244182)

