import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://comic.naver.com/webtoon/detail?titleId=747269&no=286&week=wed')

time.sleep(2)

xpath = '/html/body/div[1]/div[5]/div/div/div[5]/div[1]/div[3]/div/section/ul/li'
best_comment_elements = driver.find_elements(By.XPATH, xpath)

for li in best_comment_elements:
    try:
        comment_p = li.find_element(By.XPATH, "./div[1]/div[2]/div/p")
        comment_text = comment_p.text.strip()
        print(comment_text)
        print("-" * 30)
    except Exception as e:
        print(e)

time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div/div[5]/div[1]/div[3]/div/section/div[4]/button[2]").click()

time.sleep(2)
print('***** 전체 댓글 *****')


xpath_2 = '/html/body/div[1]/div[5]/div/div/div[5]/div[1]/div[3]/div/section/ul/li'
all_comment_elements = driver.find_elements(By.XPATH, xpath_2)
all_comment_elements
for li in all_comment_elements:
    try:
        comment_p = li.find_element(By.XPATH, "./div[1]/div[2]/div/p")
        comment_text = comment_p.text.strip()
        print(comment_text)
        print("-" * 30)
    except Exception as e:
        print("클린봇에 걸린 댓글")
        print("-" * 30)

time.sleep(2)