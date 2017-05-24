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

    def parse_child_page(self, response):
        print("--parse_child")

    def load_child_page(self, d):
        print("--parse_child")

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
            # yield item
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
