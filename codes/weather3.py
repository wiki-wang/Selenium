from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r'c:\wyy\webdrivers\chromedriver.exe')
driver.get('http://www.weather.com.cn/html/province/guangxi.shtml')
ele = driver.find_element_by_id('forecastID')
html_doc = ele.get_attribute('innerHTML')
soup = BeautifulSoup(html_doc, 'html5lib')
dls = soup.find_all('dl')

# 获取城市和最低温度，存入cityList
cityList = []
for dl in dls:
    city = dl.dt.a.string
    lowtemp = dl.find('b').string
    print(dl.name)
    lowtemp = int(lowtemp.replace('℃', ''))
    print(city, lowtemp)
    cityList.append([city, lowtemp])

# 找出最低气温和所在的城市，存入lowest和lowCities列表
lowest = None
lowCities = []
for city in cityList:
    if lowest == None or lowest > city[1]:
        lowest = city[1]
        lowCities = [city[0]]
    elif lowest == city[1]:
        lowCities.append(city[0])

print('最低气温为：{}，所在城市为:{}'.format(lowest, ','.join(lowCities)))

driver.quit()
