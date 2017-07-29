import re
import json
import logging
from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.http import Request,Response
from scrapy.spiders import CrawlSpider, Rule
import urllib
from  xingqiwang.items import *




class maijdSpider(CrawlSpider):
    name = 'xingqiwang'
    allowed_domains = ['xingqiwang.net']
    sitemap=urllib.request.urlopen('http://www.xingqiwang.net/SiteMap.Xml').read().decode('utf-8')
    nodes= re.findall('<loc>(.*?)</loc>', sitemap)
    links=[]
    for node in nodes:
        link=re.sub('<.*?>','',node)
        links.append(link)
    start_urls = links

    def parse(self, response):
        response_selector = Selector(response)
        webitem = XingqiwangItem()
        webitem['sitename'] ='www.xingqiwang.net'
        webitem['siteurl'] = 'http://www.xingqiwang.net/'
        webitem['pageurl'] = str(response.url)

        list = []
        for info in response_selector.xpath(u'//*/text()').extract():
            info = "".join(info.split())  # 去掉空白符
            list.append(info)
        text = ''.join(list)
        webitem['pagecontent'] = text
        for related_link in response_selector.xpath(u'//a/@href').extract():
            if related_link:
                    outer =(related_link.startswith('http') or related_link.startswith('www'))and self.allowed_domains[0] not in  related_link
                    if outer:
                        outer_link = related_link
                        webitem['linkurl'] = outer_link
                        yield webitem
                    else:
                        '''
                        print(related_link)
                        if related_link.startswith('/'):
                            temp=related_link.lstrip('/')
                            '''

                        inner_link= webitem['siteurl']+related_link
                        print('!!!!!!')
                        print(str(response.url))
                        print(inner_link)
                        yield Request(inner_link, callback=self.parse)

