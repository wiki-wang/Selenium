from selenium import webdriver

driver = webdriver.Chrome('c:\wyy\webdrivers\chromedriver.exe')
driver.get('https://www.51job.com/')
driver.implicitly_wait(10)

# 找到高级搜索并点击
adSearch = driver.find_element_by_css_selector('a.more')
adSearch.click()

# 找到关键字输入框并输入python
keyInput = driver.find_element_by_css_selector('p > input#kwdselectid')
keyInput.clear()
keyInput.send_keys('python')

# 设置地点
location = driver.find_element_by_id('work_position_input')
location.click()

# 如果杭州未被选中，则选中杭州
hangzhou = driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200')
import time
time.sleep(2)
if hangzhou.get_attribute('class') != 'on':
    hangzhou.click()
selectedCities = driver.find_elements_by_css_selector('#work_position_click_multiple_selected > span')

# 在城市列表中轮询，将非杭州的城市移除

for city in selectedCities:
    print(city.text)
    if city.text == '杭州':
        continue
    city.find_element_by_tag_name('em').click()
driver.find_element_by_css_selector('#work_position_click_bottom_save').click()  # 点击确定按钮
# 为避免搜索框弹出的下拉联想搜索框影响只能类别的操作，设置完地点后，重新点击一次关键字输入框
keyInput.click()

# 设置职能类别
jobType = driver.find_element_by_css_selector('#funtype_click')
jobType.click()
key1 = driver.find_element_by_id('funtype_click_center_left_each_0100')

# 如果没有选中 计算机/通信/互联网/电子，则先点击
if key1.get_attribute('class') != 'on':
    key1.click()
key2 = driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100')
key2.click()
key3 = driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106')
key3.click()
conButton = driver.find_element_by_id('funtype_click_bottom_save')
conButton.click()


# 选择公司性质
companyP = driver.find_element_by_css_selector('#cottype_list')
companyP.find_element_by_css_selector('input').click()
# 选中外资（欧美）
companyP.find_element_by_css_selector('div.ul span[data-value="01"]').click()

# 选择年限
workSpanP = driver.find_element_by_css_selector('#workyear_list')
workSpanP.find_element_by_css_selector('input').click()
workSpanP.find_element_by_css_selector('div.ul span[data-value="02"]').click()

# 选择搜索按钮并点击
driver.find_element_by_css_selector('div.btnbox.p_sou > span').click()

# 格式化输出搜索结果
for one in driver.find_elements_by_css_selector('#resultList div.el')[1:]:
    lines = one.find_elements_by_tag_name('span')
    print('|'.join([line.text for line in lines]))

driver.quit()






