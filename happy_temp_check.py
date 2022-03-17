from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
import time
import sys, os

f = open('my_information.txt', 'r', encoding='UTF8')
my_information = f.readlines()
f.close()

num = 0 # my_information의 인덱스 번호 초기화

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = './chromedriver.exe'
if os.path.exists(driver_path):
    print(f"chrom driver is insatlled: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)

driver = webdriver.Chrome(driver_path)

# 동의대학교 행복기숙사 체온 측정 구글폼
url = 'https://docs.google.com/forms/d/e/1FAIpQLSdka3B7OA0l1aj7H26bPkNynKzHaH2PahuRNdbqGpyEepCX3w/viewform'
    
driver.get(url) # 웹사이트 이동
time.sleep(1)


for i in range(1,14,4):
    xpath = '//input[@aria-labelledby="i'+str(i)+'"]'
    driver.find_element_by_xpath(xpath).send_keys(my_information[num])
    num += 1

# 기타 증세 없음 체크
xpath2 = '//*[@id="i22"]/div[2]'
driver.find_element_by_xpath(xpath2).click()

time.sleep(1)

# 제출 버튼 클릭
xpath3 = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'
driver.find_element_by_xpath(xpath3).click()

time.sleep(1)

driver.close()
