# Created by kelvin at 2018-09-16
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

comment_url = 'http://gall.dcinside.com/comment/view'


# 식물 갤러리의 게시글을 가져온다.
def get_article(article_no):
    # 게시글을 가져올 url
    article_url = 'http://gall.dcinside.com/board/view/'
    # 쿠키를 계속 유지하기 위해 사용
    session = requests.Session()
    # 사람처럼 보이게 하기 위해 다음과 같은 헤더 적용
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    gall_name = 'tree'

    params = {'id': gall_name, 'no': article_no}

    response = session.get(article_url, headers=headers, params=params)

    soup = BeautifulSoup(response.text, 'html.parser')

    user_info = soup.find(attrs={'class': 'user_layer'})

    article_title = soup.select('.wt_subject > dd')[0].get_text().strip()

    user_id = user_info['user_id'].strip()

    nickname = user_info['user_name'].strip()

    ip_address = soup.find(attrs={'class': 'li_ip'}).get_text().strip()

    view_cnt = soup.find_all(attrs={'class': 'dd_num'})[0].get_text().strip()

    comment_cnt = soup.find_all(attrs={'class': 'dd_num'})[1].get_text().strip()

    content = soup.table.td.get_text().strip()

    reg_dtime = soup.find('b').get_text().strip()

    article_data = (gall_name, article_no, article_title, user_id, nickname,
                    ip_address, view_cnt, comment_cnt, content, reg_dtime)

    print(article_data)

    f = open('dc_crawling_result.csv', 'a', encoding='utf8')
    for i in article_data:
        f.write(str(i)+", ")
    f.close()


if __name__ == "__main__":
    # http://gall.dcinside.com/board/view/?id=tree&no=243965 이 URL의 게시글을 크롤링 함.
    get_article(243965)

