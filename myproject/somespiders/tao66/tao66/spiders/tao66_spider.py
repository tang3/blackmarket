#encoding:UTF-8  
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
from tao66.items import *  
from tao66.misc.log import *

  
  
class tao66Spider(CrawlSpider):  
    name = 'tao66'
    allowed_domains = ['tao66.com']
    start_urls = ['http://bbs.tao66.com']

    def parse(self, response):
        #self.log('A response from %s just arrived!' % response.url)
        response_selector = Selector(response)
        webitem=Tao66Item()
        webitem['sitename'] = 'bbs.tao66.com'
        webitem['siteurl']='http://bbs.tao66.com'
        webitem['pageurl'] = str(response.url)

        list=[]
        for info in response_selector.xpath(u'//*/text()').extract():
            #text=node.text
            info= "".join(info.split())  # 去掉空白符
            list.append(info)
        text=''.join(list)
        #logging.info(text)
        #logging.info(len(text))
        webitem['pagecontent']=text
        '''
        print(type(response))
        list = []
        for node in response_selector.xpath(u'//*').extract():
            list.append(node)
        html='/n'.join(list)
        webitem['content'] =html
        '''
        for related_link in response_selector.xpath(u'//a/@href').extract():
            if related_link:
                #related_link.replace('\t','').replace('\r','').replace(' ','')
                related_link="".join(related_link.split())#去掉空白符
                valid_link=re.findall(r'http://.*',related_link, re.I|re.S|re.M)
                if valid_link:
                    next_link=valid_link[0]
                    inner='tao66.com'in next_link
                    if inner:
                        inner_link=next_link
                        yield Request(inner_link, callback=self.parse)
                    else:
                        outer_link=next_link
                        #print(outer_link)
                        webitem['linkurl']=outer_link
                        yield webitem
                        #yield Request(outer_link, callback=self.parse)
                        #i=i+1;
                        #print(i)
                        #print(outer_link)
                        #fp.write(str(i))
                        #fp.write('\n')
                        #fp.write(outer_link)
                        #fp.write('\n')

                
                    
                    




