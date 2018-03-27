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
                #print(i.getText())
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
                #print(i.getText())
                fp.write(j.getText().replace('\n', ''))
                fp.write('\n')

if __name__ == "__main__":

    with open("./medicine_data_character.txt", 'w',encoding="utf-8") as fp:
        for i in range(5):
            wenxing_url = "http://www.a-hospital.com/w/%E6%B8%A9%E6%80%A7%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8"
            wenxing_total_page = 27
            download_original_data(fp,  wenxing_url, wenxing_total_page)

            pingxing_url = "http://www.a-hospital.com/w/%E5%B9%B3%E6%80%A7%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8"
            pingxing_total_page = 32
            download_original_data(fp,  pingxing_url, pingxing_total_page)

            hanxing_url = "http://www.a-hospital.com/w/%E5%AF%92%E6%80%A7%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8"
            hanxing_total_page = 23
            download_original_data(fp,  hanxing_url, hanxing_total_page)

            liangxing_url = "http://www.a-hospital.com/w/%E5%87%89%E6%80%A7%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8"
            liangxing_total_page = 22
            download_original_data(fp,  liangxing_url, liangxing_total_page)

            rexing_url = "http://www.a-hospital.com/w/%E7%83%AD%E6%80%A7%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8"
            rexing_total_page = 1
            download_original_data(fp,  rexing_url, rexing_total_page)

    with open("./medicine_data_taste.txt", 'w',encoding="utf-8") as fp:
        for i in range(7):
            ganwei_url = "http://www.a-hospital.com/w/%E7%94%98%E5%91%B3%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8"
            ganwei_total_page = 35
            download_original_data(fp, ganwei_url, ganwei_total_page)

            kuwei_url = "http://www.a-hospital.com/w/%E8%8B%A6%E5%91%B3%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8"
            kuwei_total_page = 53
            download_original_data(fp, kuwei_url, kuwei_total_page)

            xinwei_url = "http://www.a-hospital.com/w/%E8%BE%9B%E5%91%B3%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8"
            xinwei_total_page = 34
            download_original_data(fp, xinwei_url, xinwei_total_page)

            suanwei_url = "http://www.a-hospital.com/w/%E9%85%B8%E5%91%B3%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8"
            suanwei_total_page = 7
            download_original_data(fp, suanwei_url, suanwei_total_page)

            xianwei_url = "http://www.a-hospital.com/w/%E5%92%B8%E5%91%B3%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8"
            xianwei_total_page = 7
            download_original_data(fp, xianwei_url, xianwei_total_page)

            sewei_url = "http://www.a-hospital.com/w/%E6%B6%A9%E5%91%B3%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8"
            sewei_total_page = 12
            download_original_data(fp, sewei_url, sewei_total_page)

            danwei_url = "http://www.a-hospital.com/w/%E6%B7%A1%E5%91%B3%E4%B8%AD%E8%8D%AF%E5%88%97%E8%A1%A8"
            danwei_total_page = 7
            download_original_data(fp, danwei_url, danwei_total_page)