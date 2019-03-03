import requests
from pyquery import PyQuery as pq

url = 'http://www.zhihu.com/explore'
headers = {
    # 'Cookie':'_zap=7d2b0dc7-e2a7-48e8-a615-0b0dee47754b; _xsrf=1ecd4216-2315-4eac-a778-378df8e541b5; d_c0="AFCoRYZTbA6PTtR69we9ZYxuERF7MDac4xk=|1540567821"; capsion_ticket="2|1:0|10:1545529660|14:capsion_ticket|44:NGQyZTJmODkyYjM1NGUyMTgxZjAyOWJkMDI2NTRiMGY=|fd53eee03926bead14a52cce278dc326391c9eaa276e6e31db821506074c015d"; l_n_c=1; r_cap_id="MjY5YTg5NTVlOGVkNGFlNmI4NGI4MGY4ODRjNTgxZDE=|1545529685|db22e2370197eb3906e543e3bf1aea2c24b3856d"; cap_id="N2NjNGRmNDk2ZGM4NDJhNzg3MzM2YmE5N2RkZTYwZDM=|1545529685|12aa51c91357779bea8fd6fd9da97cc512b0428c"; l_cap_id="OWQzNTNlMTQ0NWNhNGUxMmE4NjYzZGNlZTAyY2YzMTY=|1545529685|7ae780e698902235174e5f81134443bd628e1a4c"; n_c=1; z_c0=Mi4xX2F1bUJBQUFBQUFBVUtoRmhsTnNEaGNBQUFCaEFsVk5YVGNNWFFDQ0pjLXV1blRfVXFsMGR0dS03UDRVbkVxT0V3|1545529693|0e4289624fd14142d4bb2f5f76ccfc1771c8e8e9; tst=r; __gads=ID=6c4b84dd7949e53d:T=1545529945:S=ALNI_MbAQgLhSCfJ7A0KoQwBI-flePqImg; q_c1=9bdf7fdef47c4bab8435182730d9d70f|1547264799000|1540567822000; tgw_l7_route=1b9b7363f02f3a5519d03bdf813bc914; __utma=51854390.1146666067.1547270766.1547270766.1547270766.1; __utmb=51854390.0.10.1547270766; __utmc=51854390; __utmz=51854390.1547270766.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20170409=1^3=entry_date=20170409=1',
    # 'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
html = requests.get(url, headers = headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()



import pymysql
db = pymysql.connect(host='localhost',user='root',password='zhangwentao123')
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)