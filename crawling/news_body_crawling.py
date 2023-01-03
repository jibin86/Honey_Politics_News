from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains as ac

import requests
from bs4 import BeautifulSoup

from time import sleep
import pandas as pd
import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager



# 와인 1개의 info 얻기
def get_art_body():
    soup = BeautifulSoup(browser.page_source, "lxml")
    content = ''
    # 기사 본문
    art_body = soup.find_all('p', 'content_text')
    for art in art_body:
        content = content + '\n' + art.text
    return content


###### 브라우저 옵션 설정 ######

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

#############################

import pandas as pd
import numpy as np

df = pd.read_csv('test.csv')
print(df.shape)
art_body_list = []
df22 = df.iloc[75:,]
urls = df22['link']
for i, url in enumerate(urls):
    browser.get(url)
    art_body = get_art_body()
    art_body_list.append(art_body)
    print(f'{i}/{df22.shape[0]} \n {url} \n body 수집 완료')
df22['body'] = art_body_list

df22.to_csv("news_body2.csv")

print(' csv 저장 완료')
