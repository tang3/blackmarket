# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymysql.cursors
class CospiderPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            user='root',
            passwd='123456',
            db='mydb',
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        # insert webpage
        self.cursor.execute("""select 1 from webpages_2 where sitename = %s and pageurl=%s """,
                            (item['sitename'], item['pageurl']))
        ret2 = self.cursor.fetchone()
        if ret2:
            pass
        else:
            res2 = self.cursor.execute("""insert into webpages_2 (sitename,pageurl,pagecontent) values(%s,%s,%s)""",
                                       (item['sitename'], item['pageurl'], item['pagecontent']))
            self.connect.commit()
            # logging.info("insert")
            # logging.info(res2)
        # insert outboundlink
        self.cursor.execute("""select 1 from outboundlinks_2 where seed= %s and linkurl = %s """,
                            (item['sitename'], item['linkurl']))
        ret3 = self.cursor.fetchone()
        if ret3:
            pass
        else:
            res3 = self.cursor.execute("""insert into outboundlinks_2 (seed,linkurl) values(%s,%s)""",
                                       (item['sitename'], item['linkurl']))
            self.connect.commit()
            # logging.info("insert")
            # logging.info(res3)
        return item

    def __del__(self):
        self.connect.close()
