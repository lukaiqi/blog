import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
res = requests.get('https://ipchaxun.com/{}'.format(ip),headers=headers)
print(res)
# 解析返回的网页
html = BeautifulSoup(res.content.decode('gb2312'), 'lxml')
# 提取数据
li = html.select('.ul1 li')[0].text
addr = li.split('：')[1]
print(addr)
