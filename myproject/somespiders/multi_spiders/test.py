from urlparse3 import parse_url
from urllib.parse import  urlparse,urljoin
try:
    url ='article-598-1.html'
    url1=urlparse(url)
    url2=urljoin('http://www.tao66.com/thread-598-3.html',url)
except :
    print('ValueError')
else:
    print(len(url1.scheme))
    print(url2)
    #print(url.scheme)
    #print(url.domain)