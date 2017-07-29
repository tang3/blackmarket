#coding:utf-8
from bs4 import BeautifulSoup
import urllib
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
baseURL='http://txip8.com'
request = urllib2.Request(baseURL)
response = urllib2.urlopen(request)
homepage=response.read()
soup=BeautifulSoup(homepage,"lxml")

menu=soup.body.div.find('div',recursive=True,class_='menu')
temp=menu.find_all('a',attrs={'href':re.compile('.*?asp$',re.S)})
pages=[]
for item in temp:
    pageurl=baseURL+'/'+item.attrs['href']
    pages.append(BeautifulSoup(urllib2.urlopen(urllib2.Request(pageurl)).read(), "lxml"))
#page1_inf=pages[1].table.find_all('tr')
#for item in page1_inf:
#    print item.text
file=open( "data.txt","w+")
for i in range(1,7):
    page1_inf = pages[i].find_all('div', id='main')
    for item in page1_inf:
        file.write(item.text)
        print item.text

#page1_inf=pages[1].find_all('div',id='main')
#for item in page1_inf:
   #print item.text
#page2_inf=pages[2].find_all('div',id='main')
#for item in page2_inf:
   #print item.text
#page3_inf=pages[3].find_all('div',id='main')
#for item in page3_inf:
   #print item.text
#page4_inf=pages[4].find_all('div',id='main')
#for item in page4_inf:
   #print item.text
#page5_inf=pages[5].find_all('div',id='main')
#for item in page5_inf:
   #print item.text