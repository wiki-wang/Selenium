from selenium import webdriver

driver = webdriver.Chrome('c:\wyy\webdrivers\chromedriver.exe')

# 打开浏览器页面
driver.get('http://music.taihe.com/top/new')

import time
time.sleep(3)
ele = driver.find_element_by_id('songListWrapper')
# print(ele.text)

# 取出每一个<li>标签，判断歌曲状态，为up状态的歌曲，取出曲名、演唱者存入songList
songList = ele.find_elements_by_tag_name('li')
targetList = []  # 存储最终结果的列表

sum = 0
for song in songList:
    # print(song.text)
    status = song.find_element_by_class_name('status')
    if status.find_element_by_tag_name('i').get_attribute('class') == 'up':  # 如果状态为up，则取出歌曲名字和演唱者
        songName = song.find_element_by_class_name('song-title').text
        singer = song.find_element_by_class_name('author_list').text
        if ('主题曲'in songName) or ('电影' in songName):  # 如果歌名中含有主题曲或者电影字样，则使用（进行切割，取前部分内容
            if '（' in songName:  # 如果有中文括号隔开，则使用中文括号分割
                songName = songName.split('（')[0]
            elif '(' in songName:  # 如果有英文括号隔开，则使用英文括号分割
                songName = songName.split('(')[0]
        targetList.append([songName, singer])
        sum += 1  # 计算排名上升的歌曲数量

# 输出结果
for one in targetList:
    print('{:<12}:{:>4}'.format(one[0], one[1], chr(12288)))
print('排名上升的歌曲有{}首'.format(sum))


driver.quit()