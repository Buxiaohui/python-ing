# encoding 'utf-8'
from scrapy.spiders import Spider
import sys

sys.path.append('..')
from ..items import Spider01Item


class MokoSpider02(Spider):
    name = "MokoSpider02"
    allowed_domains = ["www.moko.com"]
    start_urls = ['http://www.moko.cc/channels/post/23/1.html', ]
    x = Spider01Item()

    def parse(self, response):
        current_url = response.url  # 爬取时请求的url
        print('current url is %s' % current_url)
        # body = response.body  # 返回的html
        # print(body)
        # '//'全局查找
        for sel in response.xpath("//ul[@class = 'post small-post']"):
            print('---sel---')
            print(sel)
            print('---sel-extract--')
            ul = sel.extract()
            # print(ul)

            # './' 当前的xpath下查找
            # 属性，用@连接
            # try:
            #     img_url = sel.xpath("./div/a/img/@src2").extract()[0]
            # except:
            #     print('img url is empty')
            # finally:
            #     print('img url is %s' % img_url)
            # if not img_url.strip():
            #     item = Spider01Item()
            #     item['url'] = img_url
            #     yield item

            print("--li---")
            print(sel.xpath("/li)"))
            # for li in sel.xpath("./li)").extract():
                # print('index is %d' % index)
                # print('li is %d' % li)
                   # if index == 0:
                   #     author = li.xpath("")
                   # if index == 1:
                   # if index == 2:

