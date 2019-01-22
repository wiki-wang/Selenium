from selenium import webdriver

driver = webdriver.Chrome(r'c:\wyy\webdrivers\chromedriver.exe')

# 访问江苏省天气网
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

import time
time.sleep(2)
ele = driver.find_element_by_id('forecastID')
var = ele.text

# 把ele.text的内容存入列表weatherList
weatherList = []
tmp = []

tmp = str(var).strip().split('\n') #tmp按[城市，温度，城市，温度]存储

# weatherList按照[[城市，温度],[城市、温度]]存储，tmp下标为偶数时为城市名字，为奇数时为温度
for i in range(0, len(tmp), 2):
    if i%2 == 0:
        lowTemp = int(tmp[i+1][:2])   # 取出最低温度
        highTemp = int(tmp[i+1][4:6])  # 取出最高温度
        weatherList.append([tmp[i], lowTemp, highTemp])

# 取出weatherList中每个城市的最低温度依次进行比较，找出最低的温度和对应城市，存入列表中


# 将第一个城市的最低温度作为最低温度
minTemp = weatherList[0][1]
cityList = []
cityList.append(weatherList[0][0])

# 依次与剩余城市的最低温度比较，若小于则替换，若等于则追加，若大于则不做改动
for i in range(1, len(weatherList)):
    if weatherList[i][1] > minTemp:  # 当前城市的最低温度大于minTemp
        continue
    elif weatherList[i][1] == minTemp:  # 当前城市的最低温度和minTemp相等
        cityList.append(weatherList[i][0])
    else:  # 当前城市的最低温度小于minTemp，将当前最低温度存入minTemp
        minTemp = weatherList[i][1]
        cityList.clear()
        cityList.append(weatherList[i][0])

# 对cityList进行处理，以字符串形式输出
cityStr = ','.join(cityList)

print('省内最低温度为{}℃，城市有{}'.format(minTemp, cityStr))

driver.quit()


