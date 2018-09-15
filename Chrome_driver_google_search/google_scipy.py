from selenium import webdriver
from bs4 import BeautifulSoup
import time  #設定間格時間避免被當成網路攻擊

#設定chromedrive
chrome_options = webdriver.ChromeOptions()

#設定為不顯示瀏覽器
chrome_options.add_argument('--headless') # 啟動無頭模式

#windowsd必須加入此行
chrome_options.add_argument('--disable-gpu') 

#設定driver路徑以及設定
driver = webdriver.Chrome(executable_path = './chromedriver',chrome_options=chrome_options)

#爬取網站
driver.get('https://www.google.com')

#找到元素q為搜尋窗口
q  = driver.find_element_by_name('q')

#搜尋目標字串
q.send_keys('Search Text')

#from selenium.webdriver.common.keys import Keys
#q.send_keys(Keys.RETURN)

q.submit()


###使用soup分析網頁
"""
soup = BeautifulSoup(driver.page_source, 'lxml')


for ele in soup.select('#rso h3 a'):
    print(ele.text)
    print(ele['href'])



driver.find_element_by_link_text('下一頁').click()
"""

#用迴圈來執行爬的頁數
for p in range(2):

    #找到下一頁的按鈕並點擊
    driver.find_element_by_link_text('下一頁').click()
    
    #取得網頁資訊
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    #找到所有標籤rso h3 a
    for ele in soup.select('#rso h3 a'):
        
        #顯示網站名稱
        print(ele.text)

        #顯示網址
        print(ele['href'])
        
    #間隔1秒
    time.sleep(1)

#爬完資料 關閉黑色視窗
driver.quit() 

