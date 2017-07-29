# -*- coding: utf-8 -*-
import sys
import urllib.request
#from scrapy.linkextractors.sgml import SgmlLinkExtractor as sle
import re
#import requests
#import gzip
#url='https://ishadow.info/'
url='http://bbs.tao66.com/'

#req=requests.get(url)
#req.encoding='utf-8'

fp=open('html2.txt','w')
response=urllib.request.urlopen(url)
#response_selector = Selector(response)
#for txt in response_selector.xpath(u'//text()').extract:
#    print(txt)
#type= response.headers.get('Content-Type')
# coding= response.headers.getparam("charset")
html=response.read().decode('gbk')#.encode('utf-8')
fp.write(html)
#gzipped = page.headers.get('Character-Encoding')
#print(gzipped)
#page=gzip.decompress(page).decode('utf-8')

'''
RegularExpression='<title>(.*)<\/title>'
Valuable=re.findall(RegularExpression,page)
for valuable in Valuable:
    valuable=re.sub('<.*?>','',valuable)
    print (valuable)
'''