# encoding 'utf-8'
import os
import urllib

import requests
from bs4 import BeautifulSoup

class Spider:
    mokoUrl = "http://www.moko.cc/channels/post/23/1.html"
    mokoBaseUrl = "http://www.moko.cc"

    def getHtml(self,url):
        r = requests.get(url)
        print(r.status_code)
        if r.status_code == 200:
            print(r.encoding)
            print(r.text)
            return r.text
        else:
            pass

    def getName(self,num, dir):
        name = '%s.jpg' % num;
        # print("----------------name---")
        print(name)
        finalName = dir + '/' + name
        print("----------------finalName---")
        print(finalName)
        return finalName

    def Mkdir(self,file_path):
        # 文件夹自动创建
        if not os.path.isdir(file_path):
            print(file_path + u' is not exists')
            print(u'Ready to create')
            os.makedirs(file_path)
            print(u'Create Success')
        else:
            print(file_path + u' is exists')

    def bs4_paraser(self,html):
        if html == '':
            return

        soup = BeautifulSoup(html, 'html.parser')
        # top lvl div of gridview
        # <div class="index-module noborder-module">
        all_div = soup.find_all('div', attrs={'class': 'index-module noborder-module'}, limit=1)
        for row in all_div:
            # print("-------1111---------")
            # print(row)
            # sec lvl div of gridview
            all_div_item = row.find_all('div', attrs={'class': 'w970'})
            for r in all_div_item:
                # each item
                # < ul class ="post small-post" >
                items = r.find_all('ul', attrs={'class': 'post small-post'})
                for item in items:
                    coverDiv = item.find_all('div', attrs={'class': 'cover'}, limit=1)
                    # print("----------------coverDiv---")
                    # print(coverDiv)
                    aTag = coverDiv[0].find("a")
                    # print("----------------linkTail---")
                    linkTail = aTag['href']
                    # print(linkTail)
                    title = aTag.img['alt']
                    # print("----------------title---")
                    # print(title)
                    dirPath = '/Users/bxh/Downloads/111/' + title
                    self.Mkdir(dirPath)
                    finalUrl = self.mokoBaseUrl + linkTail
                    # print("----------------finalUrl---")
                    # print(finalUrl)
                    detailPageHtml = self.getHtml(finalUrl)
                    if detailPageHtml is '':
                        break

                    detailSoup = BeautifulSoup(detailPageHtml, 'html.parser')
                    picboxs = detailSoup.find_all('p', attrs={'class': 'picBox'})
                    num = 0
                    for imgTag in picboxs:
                        num = num + 1
                        imgUrl = imgTag.img['src2']
                        # print("----------------imgUrl---")
                        # print(imgUrl)
                        urllib.request.urlretrieve(imgUrl, self.getName(num, dirPath))

    def __init__(self):
        htmlStr = self.getHtml(self.mokoUrl)
        self.bs4_paraser(htmlStr)

doIt = Spider()
