# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PaidaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sitename=scrapy. Field()
    siteurl=scrapy. Field()
    pageurl=scrapy. Field()
    pagecontent = scrapy. Field()
    linkurl = scrapy. Field()
