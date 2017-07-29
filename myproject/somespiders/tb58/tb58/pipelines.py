# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import pymysql.cursors
import logging
class Tb58Pipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host='30.1.30.16',
            user='root',
            passwd='123456',
            db='mydb',
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # insert website
        self.cursor.execute("""select 1 from websites where sitename = %s""", item['sitename'])
        ret1 = self.cursor.fetchone()
        if ret1:
            pass
        else:
            res1 = self.cursor.execute("""insert into websites (sitename,siteurl) values(%s,%s)""",
                                       (item['sitename'], item['siteurl']))
            self.connect.commit()
            # logging.info("insert")
            # logging.info(res1)
        # insert webpage
        self.cursor.execute("""select 1 from webpages where sitename = %s and pageurl=%s """,
                            (item['sitename'], item['pageurl']))
        ret2 = self.cursor.fetchone()
        if ret2:
            pass
        else:
            res2 = self.cursor.execute("""insert into webpages (sitename,pageurl,pagecontent) values(%s,%s,%s)""",
                                       (item['sitename'], item['pageurl'], item['pagecontent']))
            self.connect.commit()
            # logging.info("insert")
            # logging.info(res2)
        # insert outboundlink
        self.cursor.execute("""select 1 from outboundlinks where seed= %s and linkurl = %s """,
                            (item['sitename'], item['linkurl']))
        ret3 = self.cursor.fetchone()
        if ret3:
            pass
        else:
            res3 = self.cursor.execute("""insert into outboundlinks (seed,linkurl) values(%s,%s)""",
                                       (item['sitename'], item['linkurl']))
            self.connect.commit()
            # logging.info("insert")
            # logging.info(res3)
        return item

    def __del__(self):
        self.connect.close()
