# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Spider01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    hitNum = scrapy.Field()
    carrer = scrapy.Field()
    title = scrapy.Field()

    def __init__(self):
        print("init Spider01Item")
        # item['name'] = 'hahaha'
        # self.name = "hahaha"
        # print(self.items['desc'])
        # print(self.items['name'])
