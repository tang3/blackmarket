__author__ = 'qianjun.lqj'
# -*- coding: utf-8 -*-
import re
import json
import logging
from urllib.parse import  urlparse,urljoin
from bs4 import BeautifulSoup
from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from cospider.items import *



class CoSpider(CrawlSpider):
    name = 'cospider'
    allowed_domains = []
    start_urls = ['http://www.tao6.com',
                  'http://www.17ztb.com',
                  'http://www.taozhanggui.com',
                  'http://www.i7gou.com',
                  'http://www.uvtao.com',
                  'http://www.yymoban.com ',
                  'http://www.lakwdian.com',
                  'http://www.chaxiaohao.com',
                  'http://www.51w01.com',
                  'http://www.jvtuiba.com',
                  ]
    for url in start_urls:
        parsed=urlparse(url)
        allowed_domains.append(parsed.netloc)
    #fw=open('html2.txt',encoding='utf-8')

    def parse(self, response):
        response_url=str(response.url)
        response_domain=urlparse(response_url).netloc

        webitem = CospiderItem()
        webitem['sitename'] =response_domain
        #webitem['siteurl'] = self.start_urls[0]
        webitem['pageurl'] = response_url

        html=response.text
        soup=BeautifulSoup(html)

        [script.extract() for script in soup.find_all('script')]
        [style.extract() for style in soup.find_all('style')]
        formal=soup.prettify()
        #self.fw.write(str(formal))
        text=re.sub('<.*?>','',formal)
        #text=soup.text()
        text=''.join(text.split())
        webitem['pagecontent'] = text
        for node in soup.find_all('a'):
            if node:
                href=node.get('href')
                if href:
                    link="".join(href.split())
                    if link:
                        try:
                            url = urlparse(link)
                        except:
                            pass
                        else:
                            if url.netloc=='' or url.netloc in self.allowed_domains:
                                nextlink=urljoin(response_url,link)
                                yield Request(nextlink, callback=self.parse)

                            else:
                                outboundlink=link
                                webitem['linkurl'] = outboundlink
                                yield webitem

