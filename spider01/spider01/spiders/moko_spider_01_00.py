# encoding 'utf-8'
import scrapy
from scrapy.spiders import Spider
import sys

sys.path.append('..')
from ..items import Spider01Item


# from scrapy.crawler import CrawlerProcess
# from scrapy.conf import settings

class MokoSpider02(Spider):
    name = "MokoSpider02"
    allowed_domains = ["www.moko.com", "www.moko.cc"]
    base_host = "http://www.moko.cc"
    start_urls = ['http://www.moko.cc/channels/post/23/1.html', ]
    x = Spider01Item()

    def parse(self, response):
        current_url = response.url  # 爬取时请求的url
        print('current url is %s' % current_url)
        # body = response.body  # 返回的html
        # print(body)
        # '//'全局查找
        for sel in response.xpath("//ul[@class = 'post small-post']"):
            # print('---sel---')
            # print(sel)
            # print('---sel-extract--')
            # ul = sel.extract()
            # print(ul)

            # './' 当前的xpath下查找
            # 属性，用@连接
            img_url = ""
            child_url_tail = ""
            # try:
            img_url = sel.xpath("./div/a/img/@src2").extract()[0]
            child_url_tail = sel.xpath("./div/a/@href").extract()[0]
            # except:
            # print('img url error or child_url_tail error')
            # finally:
            # print('img url is %s' % img_url)
            # print('child_url_tail is %s' % child_url_tail)

            item = Spider01Item()
            # if not img_url.strip():
            try:
                print('---img url is %s' % img_url)
                print('---child_url_tail is %s' % child_url_tail)
                item['url'] = img_url
                item['chaildUrlTail'] = child_url_tail
            except Exception as e:
                print('---img url error or child_url_tail error')
                print(e)

            # print("--li---")
            li_path = sel.xpath("./li")
            # print(li_path)
            # print(li_path.extract())
            for li in li_path:
                author_label = "发布人/"
                carrer_label = "职业/"
                hit_num_label = "点击量/"
                if li.xpath("./label/text()").extract()[0] == author_label:
                    author = li.xpath("./a/text()").extract()[0]
                    print("%s is %s" % (li.xpath("./label/text()").extract()[0], author))
                    try:
                        item['author'] = author
                    except Exception as e:
                        print(e)
                if li.xpath("./label/text()").extract()[0] == carrer_label:
                    carrer = li.xpath("./span/text()").extract()[0]
                    print("%s is %s" % (li.xpath("./label/text()").extract()[0], carrer))
                    try:
                        item['carrer'] = carrer
                    except Exception as e:
                        print(e)
                if li.xpath("./label/text()").extract()[0] == hit_num_label:
                    hit_num = li.xpath("./span/text()").extract()[0]
                    print("%s is %s" % (li.xpath("./label/text()").extract()[0], hit_num))

                    try:
                        item['hitNum'] = hit_num
                    except Exception as e:
                        print(e)

            full_child_url = self.base_host + child_url_tail
            print("full_child_url is %s" % full_child_url)
            # http://www.moko.cc/post/1239879.html
            # 解析子页面，异步，无返回值
            yield scrapy.Request(url=full_child_url, meta={'item':item},callback=self.parse_child_page, errback=self.error_callback)

    def error_callback(self, response):
        print("--get child page error_callback")

    def parse_child_page(self, response):
        item = response.meta['item']
        print("--parse_child response item")
        print(item)
        print("--parse_child response")
        print("parse_child_page response is %s" % response)
        child_current_url = response.url  # 爬取时请求的url
        print("parse_child_page current_url is %s" % child_current_url)
        # body = response.body
        pList = response.xpath("//p[@class = 'picBox']/img/@src2").extract()
        print(pList)



# process = CrawlerProcess(settings)
# process.crawl(MokoSpider02)
# process.start()
