from selenium import webdriver

driver = webdriver.Chrome('c:/wyy/webdrivers/chromedriver.exe')
driver.implicitly_wait(10)

# 打开页面
driver.get('https://tinypng.com/')

#点击下载按钮
driver.find_element_by_css_selector('figure.icon').click()

import time
time.sleep(3)

# 在弹出的文件选择框中输入文件名字
import win32com.client

fileName = '1.png'
try:

    shell = win32com.client.Dispatch('WScript.Shell')
    shell.Sendkeys('c:\\' + fileName + '\r\n')

    print('File accepted!')
except:
    print('File not found!')

# 判断图片是否上传成功，最长等待10s
try:
    if driver.find_element_by_css_selector('div.progress.success'):
        print('Upload succeeded!')
except:
    print('Upload failed')

driver.quit()