# -*- coding: utf-8 -*-

# Scrapy settings for htys123 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'htys123'

SPIDER_MODULES = ['htys123.spiders']
NEWSPIDER_MODULE = 'htys123.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'htys123 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY =False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

#越过太慢的连接请求，快速进行下一网页的抓取
DOWNLOAD_TIMEOUT = 15

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

#不重复爬取相同url
DUPEFILTER_CLASS ='scrapy.dupefilters.RFPDupeFilter'#default

#广度优先爬取
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'htys123.pipelines.Htys123Pipeline': 301,
}