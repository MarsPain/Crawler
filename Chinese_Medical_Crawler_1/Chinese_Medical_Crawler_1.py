#-*-coding:utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import os
#爬虫，爬取医学百科里面的药物数据，按归经分类爬取

'''download original medical data'''
def download_original_data(fp, url, total_page):
    for i in range(total_page):
        if i==0:
            curr_url = url
            print(curr_url)
            res = urllib.request.urlopen(curr_url, timeout=60)
            html = res.read().decode('utf-8')
            data = BeautifulSoup(html, "lxml")
            name = data.select('ul:nth-of-type(3) li')
            print("result len is", len(name))
            for j in name:
                fp.write(j.getText().replace('\n', ''))
                fp.write('\n')
        else:
            curr_page = i+1
            curr_url = '%s%s%s' % (url,'/',curr_page)
            print(curr_url)
            res = urllib.request.urlopen(curr_url, timeout=60)
            html = res.read().decode('utf-8')
            data = BeautifulSoup(html, "lxml")
            name = data.select('ul:nth-of-type(1) li')
            print("result len is", len(name))
            for j in name:
                fp.write(j.getText().replace('\n', ''))
                fp.write('\n')

if __name__ == "__main__":
    dict_character = {"http://www.a-hospital.com/w/%E6%B8%A9%E6%80%A7%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8":27,
                      "http://www.a-hospital.com/w/%E5%B9%B3%E6%80%A7%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8":32,
                      "http://www.a-hospital.com/w/%E5%AF%92%E6%80%A7%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8":23,
                      "http://www.a-hospital.com/w/%E5%87%89%E6%80%A7%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8":22,
                      "http://www.a-hospital.com/w/%E7%83%AD%E6%80%A7%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8":1}

    dict_taste = {"http://www.a-hospital.com/w/%E7%94%98%E5%91%B3%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8":35,
                  "http://www.a-hospital.com/w/%E8%8B%A6%E5%91%B3%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8":53,
                  "http://www.a-hospital.com/w/%E8%BE%9B%E5%91%B3%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8":34,
                  "http://www.a-hospital.com/w/%E9%85%B8%E5%91%B3%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8":7,
                  "http://www.a-hospital.com/w/%E5%92%B8%E5%91%B3%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8":7,
                  "http://www.a-hospital.com/w/%E6%B6%A9%E5%91%B3%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8":12,
                  "http://www.a-hospital.com/w/%E6%B7%A1%E5%91%B3%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8":7}

    with open("medicine_data_character.txt", 'w',encoding="utf-8") as fp:
        for key in dict_character:
            url = key
            total_page = dict_character[key]
            download_original_data(fp, url, total_page)

    with open("medicine_data_taste.txt", 'w',encoding="utf-8") as fp:
        for key in dict_character:
            url = key
            total_page = dict_character[key]
            download_original_data(fp, url, total_page)