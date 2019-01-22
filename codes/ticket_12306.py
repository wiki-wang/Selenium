from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('c:\\wyy\\webdrivers\\chromedriver.exe')
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
driver.implicitly_wait(10)

# 填写出发城市
departureCity = driver.find_element_by_css_selector('#fromStationText')
departureCity.click()
departureCity.send_keys('南京南\n')

# 填写到达城市
destinationCity = driver.find_element_by_css_selector('#toStationText')
destinationCity.click()
destinationCity.send_keys('杭州东\n')


# 选择发车日期
driver.find_element_by_css_selector('#date_range>ul>li:nth-of-type(2)').click()

# 选择发车时间
timeSelect = Select(driver.find_element_by_css_selector('#cc_start_time'))
timeSelect.select_by_value('06001200')


# 遍历查询结果，如果二等座有票，则显示对应的车次信息
import time
time.sleep(2)

ticketList = driver.find_elements_by_css_selector("#queryLeftTable>tr[id^='ticket']>td:nth-of-type(4)")

for ticket in ticketList:
    if ticket.text not in ('--', '无'):
        print(ticket.find_element_by_xpath('./preceding-sibling::td[3]//a').text)


driver.quit()