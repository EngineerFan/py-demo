from bs4 import BeautifulSoup
import requests
import os
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 ",
}

for i in range(51, 70):
    response = requests.get("https://biaoqing233.com/hot/" + str(i), headers)
    html = BeautifulSoup(response.text, 'html.parser')
    print(html)
    dirpath = r'D:\pic'
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    for img in html.find_all('img'):
        src_url = img.get('data-original')
        if src_url:
            src_url = 'http:' + src_url
            filename = os.path.basename(src_url)
            chi_name = img.get('alt')
            print(src_url)
            chi_name = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", chi_name)
            file_suffix = os.path.splitext(filename)
            r = requests.get(src_url, headers)
            with open(dirpath + '\\' + chi_name + file_suffix[1], 'wb+') as f:
                f.write(r.content)
