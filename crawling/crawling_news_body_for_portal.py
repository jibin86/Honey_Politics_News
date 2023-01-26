import os
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

# 제목, 날짜, 본문, 기자이름, 링크 수집
def get_art_body():
    soup = BeautifulSoup(browser.page_source, "lxml")
    content = ''
    # 기사 본문
    art_body = soup.find_all('p', 'content_text')
    for art in art_body:
        content = content + '\n' + art.text

    # 기자 이름
    reporter = soup.find('span', 'author').text

    return content, reporter


# df = pd.read_csv('test.csv')
start_idx = 0
# 이미 크롤링된 파일이 있으면 그 다음부터 크롤링 시작한다.
if os.path.exists('news_body_for_portal.csv'):
    df_before = pd.read_csv('news_body_for_portal.csv')
    start_idx = df_before.tail(1)['index'].values[0] + 1
    print(start_idx)

df = pd.read_csv('news_link_for_portal.csv')
print(df.shape)
art_body_list = []
art_reporter_list = []
art_url_list = []
idx_list = []
df22 = df[df['index']>=start_idx]
urls = list(df22['link'])
idx = list(df22['index'])

try:
    for i in range(len(idx)):
        try:
            browser.get(urls[i])
        except Exception as e:
            print(e)
            break
        

        sleep(2)
        # 현재 떠있는 창 확인
        main = browser.window_handles
        # 팝업창 종료
        for w in main:
            if w != main[0]:
                browser.switch_to.window(w)
                browser.close()
                print("close window")
        browser.switch_to.window(main[0])

        art_body, art_reporter = get_art_body()
        art_url = urls[i]

        art_body_list.append(art_body)
        art_reporter_list.append(art_reporter)
        art_url_list.append(urls[i])
        idx_list.append(idx[i])
        print(f'{i}/{df22.shape[0]} \n {urls[i]} \n collect body')
# 오류가 나도 오류 나기전까지 저장하도록 한다.
finally:
    dic_new = {"index" : idx_list,"link": art_url_list, "body":art_body_list, "reporter":art_reporter_list}
    df_new = pd.DataFrame(dic_new)
    
    if not os.path.exists('news_body_for_portal.csv'):
        df_new.to_csv('news_body_for_portal.csv', index=False, mode='w', encoding='utf-8-sig')
    else:
        df_new.to_csv('news_body_for_portal.csv', index=False, mode='a', encoding='utf-8-sig', header=False)

    print('finish saving df into csv')
