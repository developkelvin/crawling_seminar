# Created by kelvin at 2018-09-16
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

article_url = 'http://gall.dcinside.com/board/view/'
comment_url = 'http://gall.dcinside.com/comment/view'

session = requests.Session()

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

gall_name = 'tree'

article_no = 243965

params = {'id': gall_name, 'no': article_no}

response = session.get(article_url, headers=headers, params=params)

soup = BeautifulSoup(response.text, 'html.parser')

a_user_info = soup.find(attrs={'class': 'user_layer'})

article_title = soup.select('.wt_subject > dd')[0].get_text().strip()

user_id = a_user_info['user_id'].strip()

nickname = a_user_info['user_name'].strip()

ip_address = soup.find(attrs={'class': 'li_ip'}).get_text().strip()

view_cnt = soup.find_all(attrs={'class': 'dd_num'})[0].get_text().strip()

comment_cnt = soup.find_all(attrs={'class': 'dd_num'})[1].get_text().strip()

content = soup.table.td.get_text().strip()

reg_dtime = soup.find('b').get_text().strip()

article_data = (gall_name, article_no, article_title, user_id, nickname,
                ip_address, view_cnt, comment_cnt, content, reg_dtime)

print(article_data)
