from selenium import webdriver

driver = webdriver.Chrome(r'c:\wyy\webdrivers\chromedriver.exe')
driver.get('http://www.weather.com.cn/html/province/guangxi.shtml')
ele = driver.find_element_by_id('forecastID')

# print(ele.get_attribute('innerHTML'))

# 获取每个城市和它的最低气温
dls = ele.find_elements_by_tag_name('dl')
cityList = []
for dl in dls:
    city = dl.find_element_by_tag_name('dt').text
    temp = dl.find_element_by_tag_name('b').text
    temp = temp.replace('℃', '')
    temp = int(temp)
    cityList.append([city, temp])

print(cityList)

# 存储最低温度及城市列表
lowest = None
lowCities = []

for city in  cityList:
    if lowest == None or city[1] < lowest:  # 如果城市列表为空，或者当前温度低于最低温度，则最低温度为当前温度，城市列表为当前城市只包含
        lowest = city[1]
        lowCities = [city[0]]
    elif lowest == city[1]:  # 如果当前气温与最低气温相等，将当前城市追加进城市列表中
        lowCities.append(city[0])

print('当前最低气温为：{}，有以下城市:{}'.format(lowest, ','.join(lowCities)))



driver.quit()