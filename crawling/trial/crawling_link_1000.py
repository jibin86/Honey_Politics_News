
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





# 페이지 스크롤하기
def page_scroll():
    # 지정한 위치로 스크롤 내리기
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') # 1080 위치로 스크롤하기
    sleep(0.1)
    # 현재 문서 높이를 가져와서 저장
    prev_height = browser.execute_script('return document.body.scrollHeight')

    # 반복 수행
    while True:
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') # 1080 위치로 스크롤하기
        sleep(0.1)

        # 현재 문서 높이를 가져와서 저장
        curr_height = browser.execute_script('return document.body.scrollHeight')
        if curr_height == prev_height:
            break
        prev_height = curr_height




# 웹페이지 해당 주소 이동

# url = "https://www.khan.co.kr/politics/president/articles" # president
# url = "https://www.khan.co.kr/politics/assembly/articles" # assembly
# url = "https://www.khan.co.kr/politics/defense-diplomacy/articles" # defense-diplomacy
# url = "https://www.khan.co.kr/politics/north-korea/articles" # north-korea
# url = "https://www.khan.co.kr/politics/election/articles" # election
url = "https://www.khan.co.kr/politics/politics-general/articles" # politics-general

category = "politics-general"
browser.get(url)
browser.maximize_window()

# page_scroll()
dic_news_list = []
titlelist = []
linklist = []
datelist = []
# 기사 500개만 수집
number = 500
range_num = number // 10 + 2


for page in range(1, range_num):
    
    # 스크롤하기
    browser.execute_script('window.scrollTo(0, 500)')

    # 창이 뜰 때까지 대기
    try:
        element = WebDriverWait(browser, 30).until(
            ec.presence_of_element_located((By.CLASS_NAME, "df-list"))
        ) 
    finally:
        pass


    # # 검색창에 입력
    # send_str = input_gu + ' ' + input_sort
    # elem.send_keys(send_str)
    # elem.send_keys(Keys.ENTER)



    # 크롤링
    soup = BeautifulSoup(browser.page_source, 'lxml')

    # 검색 방법
    # soup.find_all('div')
    # soup.find_all("div", "corp_area")
    # soup.find_all('div', {'id': 'account'})
    # text만 추출 .text

    # 태그 형식 리턴
    news_list_all = soup.find("ul", "df-list")
    # print("news_list_all",news_list_all)
    news_list = news_list_all.find_all('li')
    count = len(news_list)
    print(count)


    # 데이터 수집하기
    for i in range(count):
        # 텍스트 값 얻기
        # title = news_list[i].find('h2').get_text()
        # 속성 값 얻기
        title = news_list[i].find('a')['title']
        link = news_list[i].find('a')['href']
        date = news_list[i].find('span', 'byline').get_text()
        print(date)
        titlelist.append(title)
        linklist.append(link)
        datelist.append(date)
        
        
    # # 필요한 뉴스 개수가 다 차면 그만
    # if len(dic_news_list) >= number:
    #     break

    
    # 뉴스 다음 버튼 누르기
    eles = browser.find_elements(by=By.CSS_SELECTOR, value='#paging > *')
    if page <= 5:
        eles[page].click()
    else:
        if page % 5 == 0:
            eles[6].click()
        else:
            try:
                eles[page % 5 + 1].click()
            except:
                 break
    page += 1
    sleep(0.1)


# csv 파일로 저장하기
data = {"title" : titlelist,"link": linklist, "date":datelist}
df = pd.DataFrame(data)
df.to_csv(f"{category}_500_.csv")

print(' csv 저장 완료')