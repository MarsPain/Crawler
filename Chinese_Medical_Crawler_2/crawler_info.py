# encoding = utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pharmnet.com.cn/tcm/knowledge/detail/120855.html')
html1 = urlopen('http://www.pharmnet.com.cn/tcm/knowledge/ycrs/1_1.html')
html2 = urlopen('http://www.pharmnet.com.cn/tcm/knowledge/detail/107669.html')

bs_obj = BeautifulSoup(html2.read(), 'html.parser', from_encoding='gb18030')

t = bs_obj.find_all('td',{"class":"maintext"})
t1 = bs_obj.find('h1')
print(t1)
#print(t)
pattern1 = re.compile(r'【别名】(.+?)<br')
pattern = re.compile(r'【功能主治】(.+?)<br')
pattern2 = re.compile(r'【性味】(.+?)<br')
#【(.+?)+
str2 = pattern.findall(str(t))
str1 = pattern1.findall(str(t))
#print(str1)
#print(str)
for i in str1:
    print(i)
for i in str2:
    print(i)
html.close



