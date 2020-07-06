import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.themoviedb.org/movie?language=zh-TW"
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

res = requests.get(url=url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")
# print(soup)


title_soup1 = soup.select('div[class="card style_1"] h2')[0] # 電影介紹網頁及電影名稱
title_date = soup.select('div[class="content"] p')[1].text # 電影上映日期
print(title_soup1)
print('上映日期:' + title_date)
