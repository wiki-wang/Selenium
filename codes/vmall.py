from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome('c:\\wyy\\webdrivers\\chromedriver.exe')
driver.implicitly_wait(10)

# 窗口最大化，否则页面显示不完全
driver.maximize_window()

driver.get('https://www.vmall.com/')
# 保存主窗口handle
mainHandle = driver.current_window_handle

# 点击华外官网
driver.find_element_by_css_selector('#caibeiMsg + div.shortcut div.s-sub > ul > li:nth-child(2) > a').click()

# 跳转到华为官网页面
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if driver.current_url == 'https://consumer.huawei.com/cn/':
        break

import time
time.sleep(3)

menuEles = [one.text for one in driver.find_elements_by_css_selector('ul.clearfix.nav-cnt > li > a')]
officialStd = ['智能手机', '笔记本', '平板',  '智能穿戴', '智能家居', '更多产品', '软件应用',  '服务与支持']

# 判断华为官网的页面菜单，是否满足预期
if menuEles == officialStd:
    print('华为官网菜单内容符合预期！')
else:
    print('华为官网菜单内容不符合预期！')

# 通过调用原窗口handle，返回主页面
driver.switch_to.window(mainHandle)

# 点击华为应用市场链接
driver.find_element_by_css_selector("ul.footer-warrant-link > li > a[href='http://appstore.huawei.com/']").click()

import time
time.sleep(3)

# 跳转到华为应用市场页面
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if '华为应用市场' in driver.title:
        break

# 判断华为应用市场的页面菜单，是否满足预期
appEles = ['首页', '游戏', '软件', '专题', '品牌专区']
menuEles = [one.text for one in driver.find_elements_by_css_selector("ul.ul-nav.emo_nv.cl > li")]
if menuEles == appEles:
    print('华为应用市场菜单内容符合预期！')
else:
    print('华为应用市场菜单内容不符合预期！')

# 后退，回到主页面
driver.back()

# 验证 笔记本 & 平板 的菜单内容
# 鼠标停留事件
action = ActionChains(driver)
action.move_to_element(driver.find_element_by_css_selector("#zxnav_1 div.category-title span")).perform()

if [one.text for one in driver.find_elements_by_css_selector(
        'div[class="category-panels category-panels-1"] > ul > li')[0:3]] == ['平板电脑', '笔记本电脑', '笔记本配件']:
    print('笔记本 & 平板菜单内容符合预期！')
else:
    print('笔记本 & 平板菜单内容符合预期！')

driver.quit()



