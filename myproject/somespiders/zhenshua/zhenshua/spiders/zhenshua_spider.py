# encoding:UTF-8
import re
import json
import logging
from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from  zhenshua.items import *



class zhenshuaSpider(CrawlSpider):
    name = 'zhenshua'
    allowed_domains = ['zhenshua.com']
    start_urls = ['http://www.zhenshua.com/']

    def parse(self, response):
        response_selector = Selector(response)
        webitem = ZhenshuaItem()
        webitem['sitename'] ='www.zhenshua.com'
        webitem['siteurl'] = 'http://www.zhenshua.com/'
        webitem['pageurl'] = str(response.url)

        list = []
        for info in response_selector.xpath(u'//*/text()').extract():
            info = "".join(info.split())  # 去掉空白符
            list.append(info)
        text = ''.join(list)
        webitem['pagecontent'] = text
        for related_link in response_selector.xpath(u'//a/@href').extract():
            if related_link:
                related_link = "".join(related_link.split())  # 去掉空白符
                valid_link = re.findall(r'http://.*', related_link, re.I | re.S | re.M)
                if valid_link:
                    next_link = valid_link[0]
                    inner = 'zhenshua.com' in next_link
                    if inner:
                        inner_link = next_link
                        yield Request(inner_link, callback=self.parse)
                    else:
                        outer_link = next_link
                        webitem['linkurl'] = outer_link
                        yield webitem









