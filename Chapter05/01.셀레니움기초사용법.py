'''
requests 의 한계
- 로그인이 필요한 사이트
- 동적으로 html을 만드는 경우

selenium
- 웹 어플리케이션 테스트를 위한 도구
- 브라우저를 실제로 띄어서 사람처럼 동작하게 만들 수 있다.
'''

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 브라우저 생성
browser = webdriver.Chrome('C:/chromedriver.exe')

# 웹 사이트 열기 
browser.get('https://www.naver.com')
#로딩이 끝날 때 까지 10초까지는 기다려줌
browser.implicitly_wait(10)

# 쇼핑 메뉴 클릭하기
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2)

# 검색창 클릭
search = browser.find_element_by_css_selector('.co_srh_area .co_srh_input')
search.click()

# 검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

