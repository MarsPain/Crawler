# encoding = utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pharmnet.com.cn/tcm/knowledge/ycrs/index1.html')
# html1 = urlopen('http://www.pharmnet.com.cn/tcm/knowledge/ycrs/1_1.html')
# html2 = urlopen('http://www.pharmnet.com.cn/tcm/knowledge/detail/107669.html')

bs_obj = BeautifulSoup(html.read(), 'html.parser', from_encoding='gb18030')

t = bs_obj.find_all('table', {"style": "border-top:1px dashed #A8773F; margin:5px 35px;"})
pattern = re.compile(r'href="(.+?)"')
str1 = pattern.findall(str(t))
#print(t)

# bs_obj1 = BeautifulSoup(t)
# t1 = bs_obj1.find_all('a')
for i in str1:
    print(i)
html.close

#test